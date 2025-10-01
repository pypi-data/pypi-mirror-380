# This code is part of qredtea.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Tensor class based on pytorch; pytorch supports both CPU and GPU in one framework.
"""

# pylint: disable=abstract-method
# pylint: disable=too-many-arguments
# pylint: disable=too-many-lines
# pylint: disable=too-many-public-methods

import logging
import math
from collections.abc import Callable, Sequence
from functools import partial
from typing import Self

import numpy as np
from qtealeaves.convergence_parameters import TNConvergenceParameters
from qtealeaves.operators import TNOperators

# pylint: disable-next=no-name-in-module
from qtealeaves.tensors import QteaTensor, TensorBackend, _parse_block_size

# All imports cause problems for the build server at the moment
# * qtealeaves is lost in the conan generator somewhere
from qtealeaves.tooling.devices import _GPU_DEVICE, _XLA_DEVICE, DeviceList
from qtealeaves.tooling.mpisupport import MPI

from qredtea.tooling import (
    QRedTeaBackendLibraryImportError,
    QRedTeaError,
    QRedTeaRankError,
)
from qredtea.torchapi import DataMoverPytorch, QteaTorchTensor

try:
    import torch as to
except ImportError as exc:
    raise QRedTeaBackendLibraryImportError() from exc
try:
    import qtorch as qto
    from qtorch.quant import Quantizer
except ImportError as exc:
    raise QRedTeaBackendLibraryImportError() from exc

GPU_AVAILABLE = to.cuda.is_available()
try:
    # pylint: disable-next=unused-import
    import torch_xla

    # Okay, this is a bold assumption, but how to get the device count?
    XLA_AVAILABLE = True
    import torch_xla.core.xla_model as xm

    # xla_device is global variable, similar to GPU, we cannot select
    # a specific device if multiple are avaiable.
    # pylint: disable-next=invalid-name
    xla_device = xm.xla_device()
except ImportError:
    XLA_AVAILABLE = False
    # pylint: disable-next=invalid-name
    xla_device = None

ACCELERATOR_DEVICES = DeviceList([_GPU_DEVICE, _XLA_DEVICE])

# pylint: disable-next=invalid-name
_BLOCK_SIZE_BOND_DIMENSION, _BLOCK_SIZE_BYTE = _parse_block_size()

# pylint: disable-next=invalid-name
_USE_STREAMS = False

__all__ = [
    "QteaQTorchTensor",
    "default_qpytorch_backend",
    "set_block_size_qteaqtorchtensors",
    "QteaQuantizer",
    "set_quantizer",
    "get_gpu_available",
    "DataMoverQPytorch",
]

logger = logging.getLogger(__name__)


# pylint: disable-next=dangerous-default-value
def logger_warning(*args, storage=[]):
    """
    Singleton to avoid multiple warnings of the same type.

    **Arguments**

    warnings : list
        List of warnings already given.

    *args : arguments
        Arguments to be passed to the logger.

    **Returns**

    warnings : list
        Updated list of warnings.
    """
    if args in storage:
        return storage

    logger.warning(*args)
    storage.append(args)

    return storage


def get_gpu_available():
    """Returns boolean on availability of GPU."""
    return GPU_AVAILABLE


def set_block_size_qteaqtorchtensors(
    block_size_bond_dimension: int = None, block_size_byte: int = None
):
    """
    Allows to overwrite bond dimension decisions to enhance performance
    on hardware by keeping "better" or "consistent" bond dimensions.
    Only one of the two can be used right now.

    **Arguments**

    block_size_bond_dimension : int
        Direct handling of bond dimension.

    block_size_byte : int
        Control dimension of tensors (in SVD cuts) via blocks of bytes.
        For example, nvidia docs suggest multiples of sixteen float64
        or 32 float32 for A100, i.e., 128 bytes.
    """
    # pylint: disable-next=invalid-name,global-statement
    global _BLOCK_SIZE_BOND_DIMENSION
    # pylint: disable-next=invalid-name,global-statement
    global _BLOCK_SIZE_BYTE

    _BLOCK_SIZE_BOND_DIMENSION = block_size_bond_dimension
    _BLOCK_SIZE_BYTE = block_size_byte

    if (block_size_bond_dimension is not None) and (block_size_byte is not None):
        # We do not want to handle both of them, will be ignored lateron,
        # but raise warning as early as possible
        logger.warning(
            "Ignoring BLOCK_SIZE_BOND_DIMENSION in favor of BLOCK_SIZE_BYTE."
        )


def set_streams_qteaqtorchtensors(use_streams: bool):
    """
    Allow to decide if streams are used.

    **Arguments**

    use_streams : bool
        If True, streams will be used, otherwise we return a nullcontext even
        if streams would be possible.

    """
    # pylint: disable-next=invalid-name,global-statement
    global _USE_STREAMS

    _USE_STREAMS = use_streams


# class set_block_size_qteaqtorchtensors once to resolve if both variables
# are set
set_block_size_qteaqtorchtensors(_BLOCK_SIZE_BOND_DIMENSION, _BLOCK_SIZE_BYTE)


class QteaQuantizer(Quantizer):
    """
    Quantizer for QteaQTorchTensor. This is a wrapper around the qtorch quantizer,
    which is used to quantize the tensor. Simply adds access to the low-precision
    numbers used in the quantization.

    Parameters
    ----------
    forward_number : qtorch.Number, optional
        The low-precision number used in the forward pass.
        Default to None.
    backward_number : qtorch.Number, optional
        The low-precision number used in the backward pass.
        Default to None.
    forward_rounding : str, optional
        The rounding method used in the forward pass.
        Default to "stochastic".
    backward_rounding : str, optional
        The rounding method used in the backward pass.
        Default to "stochastic
    """

    def __init__(
        self,
        forward_number: qto.Number = None,
        backward_number: qto.Number = None,
        forward_rounding: str = "stochastic",
        backward_rounding: str = "stochastic",
    ):
        super().__init__(
            forward_number=forward_number,
            backward_number=backward_number,
            forward_rounding=forward_rounding,
            backward_rounding=backward_rounding,
        )

        self._forward_number = forward_number
        self._backward_number = backward_number
        self._forward_rounding = forward_rounding
        self._backward_rounding = backward_rounding

    @property
    def forward_number(self):
        "The low-precision number used in the forward pass."
        return self._forward_number

    @property
    def backward_number(self):
        "The low-precision number used in the backward pass."
        return self._backward_number

    @property
    def forward_rounding(self):
        "The rounding method used in the forward pass."
        return self._forward_rounding

    @property
    def backward_rounding(self):
        "The rounding method used in the backward pass."
        return self._backward_rounding


# pylint: disable-next=too-few-public-methods
class QteaComplexQuantizer(QteaQuantizer):
    """
    Quantizer for complex numbers.

    Details
    -------
    For complex numbers, we need to quantize the real and imaginary part
    separately. This is done by calling the quantizer twice. The quantizer
    is expected to be a function that takes a tensor and returns a tensor.
    """

    def __init__(self, quantizer: QteaQuantizer):
        super().__init__(
            quantizer.forward_number,
            quantizer.backward_number,
            quantizer.forward_rounding,
            quantizer.backward_rounding,
        )

    def forward(self, x: to.Tensor):
        """Quantize the tensor."""
        return self.quantize(to.real(x)) + 1j * self.quantize(to.imag(x))


_QUANTIZER = QteaQuantizer()
_USER_SET_QUANTIZER = False


def set_quantizer(quantizer: QteaQuantizer):
    """
    Set the quantizer for the backend.

    **Arguments**

    quantizer : instance of :class:`qtorch.quant.Quantizer`
        Quantizer to be used for the backend.
    """

    # pylint: disable-next=global-statement
    global _QUANTIZER
    # pylint: disable-next=global-statement
    global _USER_SET_QUANTIZER

    _QUANTIZER = quantizer
    _USER_SET_QUANTIZER = True


class QteaQTorchTensor(QteaTorchTensor):
    """
    Tensor for Quantum TEA based on the QPyTorch tensors.
    """

    available_dtypes = (to.float32, to.complex64)

    def __init__(
        self,
        links: Sequence[int],
        ctrl: str = "Z",
        are_links_outgoing: None = None,  # pylint: disable=unused-argument
        base_tensor_cls: None = None,  # pylint: disable=unused-argument
        dtype: to.dtype = to.complex64,
        device: str = None,
        requires_grad: bool = None,
    ):

        if dtype not in self.available_dtypes:
            raise QRedTeaError(
                "Only float32 and complex64 are supported in QteaQTorchTensor."
            )

        if not _USER_SET_QUANTIZER:
            logger_warning(
                "No quantizer set, using default quantizer from qtorch (identity)."
            )

        # In principle we could add a check in the quantizer if the dtype is
        # complex or float, but we do not want to add this overhead.
        self._quantizer = (
            _QUANTIZER if dtype.is_floating_point else QteaComplexQuantizer(_QUANTIZER)
        )

        self._float_quantizer = _QUANTIZER

        super().__init__(
            links=links,
            ctrl=ctrl,
            dtype=dtype,
            device=device,
            requires_grad=requires_grad,
        )

        # NOTE: the super init calls convert, if we quantize there this can be avoided
        if ctrl is not None:
            self.quantize()

    # --------------------------------------------------------------------------
    #                               Properties
    # --------------------------------------------------------------------------

    @property
    def quantizer(self) -> QteaQuantizer:
        """Quantizer used for the tensor."""
        return self._quantizer

    @property
    def float_quantizer(self) -> QteaQuantizer:
        """Quantizer used for the tensor of float dtype (singvals,...)."""
        return self._float_quantizer

    @property
    def dtype_eps(self):
        """
        Data type's machine precision. This is the difference between 1 and the
        smallest number greater than 1 that is representable in the data type.
        Notice that, in general, this is not the spacing between a generic number
        and the next representable number, which can depend on the magnitude.
        E.g., for float32, this is 2**(-23)=~1.19e-7.

        """

        forward_number = self._quantizer.forward_number

        if forward_number is None:
            # return the machine precision of the data type
            return to.finfo(self.dtype).eps

        if isinstance(forward_number, qto.FloatingPoint):
            return 2 ** (-forward_number.man)
        if isinstance(forward_number, qto.BlockFloatingPoint):
            # from qtorch source code it seems that 2 bits are used for
            # other stuff, so we have to subtract 2. Have to double check.
            return 2 ** (-forward_number.wl + 2)
        if isinstance(forward_number, qto.FixedPoint):
            # `fl` is the number of fractional bits. In this specific case,
            # the spacing does not depend on the magnitude of the number.
            return 2 ** (-forward_number.fl)

        raise ValueError("Unknown number type")

    # --------------------------------------------------------------------------
    #                    Data type tooling beyond properties
    # --------------------------------------------------------------------------

    def dtype_from_char(self, dtype: str) -> to.dtype:
        """Resolve data type from chars C, S."""
        if dtype not in ["C", "S"]:
            raise QRedTeaError(f"Data type {dtype} not supported in QteaQTorchTensor.")
        data_types = {
            "C": to.complex64,
            "S": to.float32,
        }

        return data_types[dtype]

    # inherits `dtype_from_mpi`
    # inherits `dtype_real`
    # inherits `dtype_to_char`

    # --------------------------------------------------------------------------
    #                          Overwritten operators
    # --------------------------------------------------------------------------
    #
    # inherit def __eq__
    # inherit def __ne__

    def __add__(self, other: Self) -> Self:
        """
        Addition of a scalar to a tensor adds it to all the entries.
        If other is another tensor, elementwise addition if they have the same shape
        """

        return super().__add__(other).quantize()

    def __iadd__(self, other: Self) -> Self:
        """In-place addition of tensor with tensor or scalar (update)."""

        return super().__iadd__(other).quantize()

    def __imul__(self, factor: float | int | complex) -> Self:
        """In-place multiplication of tensor with scalar (update)."""

        return super().__imul__(factor).quantize()

    def __itruediv__(self, factor: float | int | complex) -> Self:
        """In-place division of tensor with scalar (update)."""

        return super().__itruediv__(factor).quantize()

    def __sub__(self, other: Self) -> Self:
        """
        Subtraction of a scalar to a tensor subtracts it to all the entries.
        If other is another tensor, elementwise subtraction if they have the same shape
        """

        return super().__sub__(other).quantize()

    # --------------------------------------------------------------------------
    #                       classmethod, classmethod like
    # --------------------------------------------------------------------------

    @staticmethod
    def convert_operator_dict(
        op_dict: TNOperators,
        params: dict = None,
        symmetries: list = None,
        generators: list = None,
        base_tensor_cls: None = None,
        dtype: to.dtype = to.complex64,
        device="cpu",
    ) -> TNOperators:
        """
        Iterate through an operator dict and convert the entries. Converts as well
        to rank-4 tensors.

        **Arguments**

        op_dict : instance of :class:`TNOperators`
            Contains the operators as xp.ndarray.

        params : dict, optional
            To resolve operators being passed as callable.

        symmetries:  list, optional, for compatability with symmetric tensors.
            Must be empty list.

        generators : list, optional, for compatability with symmetric tensors.
            Must be empty list.

        base_tensor_cls : None, optional, for compatability with symmetric tensors.
            No checks on this one here.

        dtype : data type for xp, optional
            Specify data type.
            Default to `to.complex64`

        device : str
            Device for the simulation. Available "cpu" and "gpu"
            Default to "cpu"

        **Details**

        The conversion to rank-4 tensors is useful for future implementations,
        either to support adding interactions with a bond dimension greater than
        one between them or for symmetries. We add dummy links of dimension one.
        The order is (dummy link to the left, old link-1, old link-2, dummy link
        to the right).
        """
        qteatensor_dict = QteaTensor.convert_operator_dict(
            op_dict,
            params=params,
            symmetries=symmetries,
            generators=generators,
            base_tensor_cls=base_tensor_cls,
            dtype=np.complex64,
            device="cpu",
        )

        new_op_dict = TNOperators(
            set_names=qteatensor_dict.set_names,
            mapping_func=qteatensor_dict.mapping_func,
        )
        for key, value in qteatensor_dict.items():
            new_op_dict[key] = QteaQTorchTensor.from_qteatensor(value)
            new_op_dict[key].convert(dtype, device)

        return new_op_dict

    # --------------------------------------------------------------------------
    #                            Checks and asserts
    # --------------------------------------------------------------------------
    #

    def are_equal(self, other, tol=1e-7):
        """Check if two tensors are equal."""

        dtype_tol = self.dtype_eps * 10

        if dtype_tol > tol:
            logger.warning(
                "Tolerance is smaller than dtype_eps %s < %s, using dtype_eps.",
                tol,
                self.dtype_eps,
            )
            tol = dtype_tol

        return super().are_equal(other, tol)

    def assert_identity(self, tol=1e-7):
        """Check if tensor is an identity matrix."""

        dtype_tol = self.dtype_eps * 10

        if dtype_tol > tol:
            logger.warning(
                "Tolerance is smaller than dtype_eps %s < %s, using dtype_eps.",
                tol,
                self.dtype_eps,
            )
            tol = dtype_tol

        super().assert_identity(tol)

    def is_close_identity(self, tol=1e-7):
        """Check if rank-2 tensor is close to identity."""

        dtype_tol = self.dtype_eps * 10

        if dtype_tol > tol:
            logger.warning(
                "Tolerance is smaller than dtype_eps %s < %s, using dtype_eps.",
                tol,
                self.dtype_eps,
            )
            tol = dtype_tol

        return super().is_close_identity(tol)

    # --------------------------------------------------------------------------
    #                       Single-tensor operations
    # --------------------------------------------------------------------------
    #
    # inherit def flip_links_update

    # pylint: disable-next=unused-argument
    def convert(
        self, dtype: to.dtype = None, device: str = None, stream: to.cuda.Stream = None
    ) -> Self:
        """
        Convert underlying array to the specified data type and/or device inplace.
        Updates also the quantizer to enable changing quantization.
        """

        if dtype is not None and dtype not in self.available_dtypes:
            raise QRedTeaError(f"Data type {dtype} not supported in QteaQTorchTensor.")

        old_eps = self.dtype_eps
        if dtype is None:
            self._quantizer = (
                _QUANTIZER
                if self.dtype.is_floating_point
                else QteaComplexQuantizer(_QUANTIZER)
            )
        else:
            self._quantizer = (
                _QUANTIZER
                if dtype.is_floating_point
                else QteaComplexQuantizer(_QUANTIZER)
            )

        # raise warning if the quantized dtype eps changed
        # using old dtype eps as tolerance
        if abs(old_eps - self.dtype_eps) > old_eps:
            logger_warning(
                "The machine precision of the data type set by the quantizer "
                + "has changed from %s to %s. this might lead to "
                + "unexpected behavior.",
                old_eps,
                self.dtype_eps,
            )

        super().convert(dtype, device, stream)
        return self

    def convert_singvals(
        self, singvals: to.Tensor, dtype: to.dtype, device: str
    ) -> to.Tensor:
        """Convert the singular values via a tensor."""
        if dtype is not None and dtype not in self.available_dtypes:
            raise QRedTeaError(f"Data type {dtype} not supported in QteaQTorchTensor.")

        singvals = super().convert_singvals(singvals, dtype, device)
        return singvals

    def diag(self, real_part_only: bool = False, do_get: bool = False) -> to.Tensor:
        """Return the diagonal as array of rank-2 tensor."""

        return (
            self._float_quantizer(super().diag(real_part_only, do_get))
            if real_part_only
            else self._quantizer(super().diag(real_part_only, do_get))
        )

    def eig_api(
        self,
        matvec_func: Callable,
        links: Sequence[int],
        conv_params: TNConvergenceParameters,
        args_func=None,
        kwargs_func=None,
    ) -> tuple[to.Tensor, to.Tensor]:
        """
        Interface to hermitian eigenproblem

        **Arguments**

        matvec_func : callable
            Mulitplies "matrix" with "vector"

        links : links according to :class:`QteaTensor`
            Contain the dimension of the problem.

        conv_params : instance of :class:`TNConvergenceParameters`
            Settings for eigenproblem with Arnoldi method.

        args_func : arguments for matvec_func

        kwargs_func : keyword arguments for matvec_func

        **Returns**

        eigenvalues : scalar

        eigenvectors : instance of :class:`QteaTensor`
        """
        val, vec = super().eig_api(
            matvec_func, links, conv_params, args_func, kwargs_func
        )

        # singvals should be real, while vec should have same dtype as self
        return self._float_quantizer(val), self._quantizer(vec)

    def eig_api_qtea(
        self,
        matvec_func: Callable,
        conv_params: TNConvergenceParameters,
        args_func=None,
        kwargs_func=None,
    ) -> tuple[to.Tensor, to.Tensor]:
        """
        Interface to hermitian eigenproblem via qtealeaves.solvers. Arguments see `eig_api`.
        """
        val, vec = super().eig_api_qtea(
            matvec_func, conv_params, args_func, kwargs_func
        )

        return self._float_quantizer(val), self._quantizer(vec)

    def eig_api_arpack(
        self,
        matvec_func: Callable,
        links: Sequence[int],
        conv_params: TNConvergenceParameters,
        args_func=None,
        kwargs_func=None,
    ) -> tuple[to.Tensor, to.Tensor]:
        """
        Interface to hermitian eigenproblem via Arpack. Arguments see `eig_api`.
        Possible implementation is https://github.com/rfeinman/Torch-ARPACK.
        """
        val, vec = super().eig_api_arpack(
            matvec_func, links, conv_params, args_func, kwargs_func
        )
        return self._float_quantizer(val), self._quantizer(vec)

    def norm(self) -> to.Tensor:
        """Calculate the norm of the tensor <tensor|tensor>."""
        return self._float_quantizer(self.norm_sqrt() ** 2)

    def norm_sqrt(self) -> to.Tensor:
        """
        Calculate the square root of the norm of the tensor,
        i.e., sqrt( <tensor|tensor>).
        """

        return self._float_quantizer(super().norm_sqrt())

    def normalize(self) -> Self:
        """Normalize tensor with sqrt(<tensor|tensor>)."""

        return super().normalize().quantize()

    def quantize(self):
        """Quantize the tensor inplace."""
        self._elem = self._quantizer(self._elem)
        return self

    def scale_link_update(
        self,
        link_weights: np.ndarray | to.Tensor,
        link_idx: int,
        do_inverse: bool = False,
    ) -> Self:
        """
        Scale tensor along one link at `link_idx` with weights (inplace update).

        **Arguments**

        link_weights : np.ndarray
            Scalar weights, e.g., singular values.

        link_idx : int
            Link which should be scaled.

        do_inverse : bool, optional
            If `True`, scale with inverse instead of multiplying with
            link weights.
            Default to `False`
        """

        return super().scale_link_update(link_weights, link_idx, do_inverse).quantize()

    # we put this to inform user of the different signature
    # pylint: disable-next=useless-parent-delegation
    def set_subtensor_entry(
        self, corner_low: Sequence[int], corner_high: Sequence[int], tensor: Self
    ):
        """
        Set a subtensor (potentially expensive as looping explicitly, inplace update).

        **Arguments**

        corner_low : list of ints
            The lower index of each dimension of the tensor to set. Length
            must match rank of tensor `self`.

        corner_high : list of ints
            The higher index of each dimension of the tensor to set. Length
            must match rank of tensor `self`.

        tensor : :class:`QteaQTorchTensor`
           Tensor to be set as subtensor. Rank must match tensor `self`.
           Dimensions must match `corner_high - corner_low`.

        **Examples**

        To set the tensor of shape 2x2x2 in a larger tensor `self` of shape
        8x8x8 the corresponing call is in comparison to a numpy syntax:

        * self.set_subtensor_entry([2, 4, 2], [4, 6, 4], tensor)
        * self[2:4, 4:6, 2:4] = tensor

        To be able to work with all ranks, we currently avoid the numpy
        syntax in our implementation.
        """
        super().set_subtensor_entry(corner_low, corner_high, tensor)
        # self.quantize()

    def trace(self, return_real_part=False, do_get=False):
        """Take the trace of a rank-2 tensor."""
        return (
            self._float_quantizer(super().trace(return_real_part, do_get))
            if return_real_part
            else self._quantizer(super().trace(return_real_part, do_get))
        )

    def expm(self, fuse_point: int = None, prefactor: float = 1) -> Self:
        """
        Take the matrix exponential with a scalar prefactor, Exp(prefactor * self).
        Reshapes the tensor into a matrix by fusing links up to INCLUDING fuse_point
        into one, and links after into the second dimension.

        To compute the exponential of a 4-leg tensor by fusing (0,1),(2,3),
        set fuse_point=1.
        """
        prefactor = self._float_quantizer(prefactor)
        return super().expm(fuse_point, prefactor).quantize()

    # --------------------------------------------------------------------------
    #                         Two-tensor operations
    # --------------------------------------------------------------------------

    def add_update(
        self,
        other: Self,
        factor_this: int | float | complex = None,
        factor_other: int | float | complex = None,
    ) -> Self:
        """
        Inplace addition as `self = factor_this * self + factor_other * other`.

        **Arguments**

        other : same instance as `self`
            Will be added to `self`. Unmodified on exit.

        factor_this : scalar
            Scalar weight for tensor `self`.

        factor_other : scalar
            Scalar weight for tensor `other`
        """

        return super().add_update(other, factor_this, factor_other).quantize()

    def dot(self, other: to.Tensor) -> to.Tensor:
        """Inner product of two tensors <self|other>."""
        return self._quantizer(super().dot(other))

    # pylint: disable=invalid-name
    def stack_first_and_last_link(self, other: Self) -> Self:
        """Stack first and last link of tensor targeting MPS addition."""

        return super().stack_first_and_last_link(other).quantize()

    # --------------------------------------------------------------------------
    #                       Gradient descent: backwards propagation
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    #                        Internal methods
    # --------------------------------------------------------------------------
    #
    # inherit _invert_link_selection

    # --------------------------------------------------------------------------
    #                                MISC
    # --------------------------------------------------------------------------

    @staticmethod
    def get_default_datamover():
        """The default datamover compatible with this class."""
        return DataMoverPytorch()

    # --------------------------------------------------------------------------
    #                 Methods needed for _AbstractQteaBaseTensor
    # --------------------------------------------------------------------------

    def assert_diagonal(self, tol: float = None):
        """Check that tensor is a diagonal matrix up to tolerance."""

        if tol is None:
            tol = self.dtype_eps * 10

        super().assert_diagonal(tol)

    def assert_int_values(self, tol: float = None):
        """Check that there are only integer values in the tensor."""

        if tol is None:
            tol = self.dtype_eps * 10
        super().assert_int_values(tol)

    def assert_real_valued(self, tol=None):
        """Check that all tensor entries are real-valued."""

        if tol is None:
            tol = self.dtype_eps * 10
        super().assert_real_valued(tol)

    @classmethod
    def from_elem_array(
        cls, tensor: np.ndarray | to.Tensor, dtype: to.dtype = None, device: str = None
    ) -> Self:
        """
        New QteaQTorchTensor from array

        **Arguments**

        tensor : to.tensor
            Array for new tensor.

        dtype : data type, optional
            Can allow to specify data type.
            If not `None`, it will convert.
            Default to `None`
        """
        # pylint: disable-next=invalid-name,global-variable-not-assigned
        global xla_device

        if isinstance(tensor, np.ndarray):
            if not tensor.flags["WRITEABLE"]:
                # Avoids torch warning if numpy side is not writeable
                tensor = tensor.copy()
            tensor = to.from_numpy(tensor)

        if dtype not in [to.float32, to.complex64, None]:
            raise QRedTeaError(f"Data type {dtype} not supported in QteaQTorchTensor.")

        if isinstance(tensor, np.ndarray):
            tensor = to.from_numpy(tensor)

        if dtype is None:
            orig_dtype = tensor.dtype
            if orig_dtype.is_complex:
                if orig_dtype == to.complex128:
                    logger_warning(
                        "The tensor dtype is complex128, will be casto to complex64 \
                        possibly losing precision"
                    )
                dtype = to.complex64
            elif orig_dtype.is_floating_point:
                if orig_dtype == to.float64:
                    logger_warning(
                        "The tensor dtype is float64, will be cast to float32, possibly \
                        losing precision"
                    )
                dtype = to.float32
            else:
                logger_warning(
                    "The tensor dtype %s is not supported and will be cast to float32, \
                    possibly leading to undefined behavior",
                    orig_dtype,
                )
                dtype = to.float32

        if device is None:
            # We can actually check with torch where we are running
            device = cls.device_str(tensor)

            if cls.is_xla_static(device):
                device = xla_device

        obj = cls(tensor.shape, ctrl=None, dtype=dtype, device=device)
        obj._elem = tensor

        obj.convert(dtype, device)
        obj.quantize()
        return obj

    def get_attr(self, *args) -> tuple[Callable]:
        """High-risk resolve attribute for an operation on an elementary array."""
        attributes = []

        for elem in args:
            if elem == "cumsum":
                # Special treatment for cumsum to resolve additional argument which
                # is not present in numpy
                attributes.append(_cumsum_like_numpy)
            elif elem == "log":
                # Special treatment to allow integers
                attributes.append(_log_like_numpy)
            elif elem == "sum":
                # Special treatment for cumsum to resolve additional argument which
                # is not present in numpy
                attributes.append(_sum_like_numpy)
            elif not hasattr(to, elem):
                raise QRedTeaError(
                    f"This tensor's elementary array does not support {elem}."
                )
            else:
                attributes.append(partial(quantization_wrapper, func=getattr(to, elem)))

        if len(attributes) == 1:
            return attributes[0]

        return tuple(attributes)

    def _truncate_singvals(
        self,
        singvals: np.ndarray | to.Tensor,
        conv_params: TNConvergenceParameters = None,
    ) -> tuple[int, to.Tensor | np.ndarray, to.Tensor | np.ndarray]:
        """
        Truncate the singular values followling the
        strategy selected in the convergence parameters class

        Parameters
        ----------
        singvals : np.ndarray
            Array of singular values
        conv_params : :py:class:`TNConvergenceParameters`, optional
            Convergence parameters to use in the procedure. If None is given,
            then use the default convergence parameters of the TN.
            Default to None.

        Returns
        -------
        cut : int
            Number of singular values kept
        singvals_kept : np.ndarray
            Normalized singular values kept
        singvals_cutted : np.ndarray
            Normalized singular values cutted
        """

        cut, singvals_kept, singvals_cutted = super()._truncate_singvals(
            singvals, conv_params
        )

        singvals_kept = self._float_quantizer(singvals_kept)
        singvals_cutted = self._float_quantizer(singvals_cutted)

        return cut, singvals_kept, singvals_cutted

    # --------------------------------------------------------------------------
    #             Internal methods (not required by abstract class)
    # --------------------------------------------------------------------------

    def dtype_mpi(self):
        """Resolve the dtype for sending tensors via MPI"""
        return {
            # pylint: disable=c-extension-no-member
            "C": MPI.COMPLEX,
            "S": MPI.REAL,
            # pylint: enable=c-extension-no-member
        }[self.dtype_to_char()]

    def _xla_norm_sqrt(self):
        """Avoid problems with complex numbers and vector norm."""
        return self._float_quantizer(super()._xla_norm_sqrt())

    def _split_qr_dim(
        self, rows: Sequence[int], cols: Sequence[int]
    ) -> tuple[Self, Self]:
        """Split via QR knowing dimension of rows and columns."""

        # we skip the check on half precision as it is not supported by QPyTorch
        # and should not be used in the first place.

        # pylint: disable-next=not-callable
        qmat, rmat = to.linalg.qr(self._elem.reshape(rows, cols))

        qtens = self.from_elem_array(qmat, dtype=self.dtype, device=self.device)
        rtens = self.from_elem_array(rmat, dtype=self.dtype, device=self.device)

        return qtens, rtens

    # pylint: disable-next=unused-argument
    def _split_svd_eigvl(
        self,
        matrix: to.Tensor,
        svd_ctrl: str,
        max_bond_dimension: int,
        contract_singvals: str,
    ) -> tuple[to.Tensor, to.Tensor, to.Tensor]:
        """
        SVD of the matrix through an eigvenvalue decomposition.

        Parameters
        ----------
        matrix: to.Tensor
            Matrix to decompose
        svd_crtl : str
            If "E" normal eigenvalue decomposition. If "X" use the sparse.
        max_bond_dimension : int
            Maximum bond dimension
        contract_singvals: str
            Whhere to contract the singular values

        Returns
        -------
        to.Tensor
            Matrix U
        to.Tensor
            Singular values
        to.Tensor
            Matrix V^dagger

        Details
        -------

        We use ᵀ*=^†, the adjoint.

        - In the contract-to-right case, which means:
          H = AAᵀ* = USV Vᵀ*SUᵀ* = U S^2 Uᵀ*
          To compute SVᵀ* we have to use:
          A = USVᵀ* -> Uᵀ* A = S Vᵀ*
        - In the contract-to-left case, which means:
          H = Aᵀ*A = VSUᵀ* USVᵀ* = VS^2 Vᵀ*
          First, we are given V, but we want Vᵀ*. However, let's avoid double work.
          To compute US we have to use:
          A = USVᵀ* -> AV = US
          Vᵀ* = right.T.conj()   (with the conjugation done in place)
        """

        left, singvals, right = super()._split_svd_eigvl(
            matrix, svd_ctrl, max_bond_dimension, contract_singvals
        )

        left = self._quantizer(left)
        singvals = self._float_quantizer(singvals)
        right = self._quantizer(right)

        return left, singvals, right

    def _split_svd_normal(
        self, matrix: to.Tensor
    ) -> tuple[to.Tensor, to.Tensor, to.Tensor]:
        """
        Normal SVD of the matrix. First try the faster gesdd iterative method.
        If it fails, resort to gesvd.

        Parameters
        ----------
        matrix: to.Tensor
            Matrix to decompose

        Returns
        -------
        to.Tensor
            Matrix U
        to.Tensor
            Singular values
        to.Tensor
            Matrix V^dagger
        """

        mat_left, singvals_tot, mat_right = super()._split_svd_normal(matrix)

        mat_left = self._quantizer(mat_left)
        singvals_tot = self._float_quantizer(singvals_tot)
        mat_right = self._quantizer(mat_right)

        return mat_left, singvals_tot, mat_right

    def _split_svd_random(
        self, matrix: to.Tensor, max_bond_dimension: int
    ) -> tuple[to.Tensor, to.Tensor, to.Tensor]:
        """
        SVD of the matrix through a random SVD decomposition
        as prescribed in page 227 of Halko, Martinsson, Tropp's 2011 SIAM paper:
        "Finding structure with randomness: Probabilistic algorithms for constructing
        approximate matrix decompositions"

        Parameters
        ----------
        matrix: to.Tensor
            Matrix to decompose
        max_bond_dimension : int
            Maximum bond dimension

        Returns
        -------
        to.Tensor
            Matrix U
        to.Tensor
            Singular values
        to.Tensor
            Matrix V^dagger
        """

        left, singvals, right = super()._split_svd_random(matrix, max_bond_dimension)

        left = self._quantizer(left)
        singvals = self._float_quantizer(singvals)
        right = self._quantizer(right)

        return left, singvals, right


def _cumsum_like_numpy(array: to.Tensor, axis: Sequence[int] | None = None, **kwargs):
    """Provide cumsum function with same arguments as numpy."""
    # numpy has default of axis=None which acts on the flattened array
    # which torch does not support
    if axis is None and array.ndim != 1:
        raise QRedTeaRankError("Running cumsum without axis on tensor with rank != 1.")

    if axis is None:
        axis = 0
    quantizer = (
        _QUANTIZER
        if array.dtype.is_floating_point
        else QteaComplexQuantizer(_QUANTIZER)
    )
    return quantizer(to.cumsum(array, axis, **kwargs))


def _log_like_numpy(array: to.Tensor):
    """Provide log function accepting as well scalar integers not being a tensor."""
    if isinstance(array, to.Tensor):
        result = to.log(array)
    else:
        result = math.log(array)

    quantizer = (
        _QUANTIZER
        if array.dtype.is_floating_point
        else QteaComplexQuantizer(_QUANTIZER)
    )

    return quantizer(result)


def _sum_like_numpy(array: to.Tensor, axis: Sequence[int] | None = None, **kwargs):
    """Provide sum function with same arguments as numpy."""
    # numpy has default of axis=None which acts on the flattened array
    # which torch does not support
    if axis is None:
        result = to.sum(array, **kwargs)
    else:
        result = to.sum(array, axis, **kwargs)

    quantizer = (
        _QUANTIZER
        if array.dtype.is_floating_point
        else QteaComplexQuantizer(_QUANTIZER)
    )

    return quantizer(result)


class DataMoverQPytorch(DataMoverPytorch):
    """
    Data mover to move QteaQTorchTensor between numpy and cupy
    """

    tensor_cls = (QteaQTorchTensor,)

    @property
    def device_memory(self):
        """Current memory occupied in the device"""
        # return self.mempool.used_bytes()
        raise NotImplementedError("Qpytorch data mover")


def default_qpytorch_backend(device="cpu", dtype=to.complex64):
    """
    Generate a default tensor backend for dense tensors, i.e., with
    a :class:`QteaQTorchTensor`.

    Parameters
    ----------
    dtype : data type, optional
        Data type for pytorch.
        Default to to.complex64

    device : device specification, optional
        Default to `"cpu"`.
        Available: `"cpu", "gpu", "xla"`

    Returns
    -------
    tensor_backend : :class:`TensorBackend`
    """
    tensor_backend = TensorBackend(
        tensor_cls=QteaQTorchTensor,
        base_tensor_cls=QteaQTorchTensor,
        device=device,
        dtype=dtype,
        symmetry_injector=None,
        datamover=DataMoverQPytorch(),
    )

    return tensor_backend


def quantization_wrapper(*args, func: Callable, **kwargs):
    """
    Wrapper to quantize the output of a function.

    Parameters
    ----------
    func : callable
        Function to be wrapped.

    *args, **kwargs
        Arguments to be passed to the function.

    Returns
    -------
    output : to.Tensor
        Output of the function, quantized.

    Details
    -------
    This tries to quantize the output of a function. If the output is a tensor
    of float32 or complex64, it quantizes it. If the output is a tuple, it quantizes
    all the tensors in the tuple with dtype float32 or complex64. Otherwise it
    returns the output as is.
    This is a guess on the output of the function, and it might not work for all
    functions.
    """
    output = func(*args, **kwargs)
    quantizer = (
        _QUANTIZER
        if output.dtype.is_floating_point
        else QteaComplexQuantizer(_QUANTIZER)
    )

    if isinstance(output, to.Tensor):
        if output.dtype in [to.float32, to.complex64]:
            return quantizer(output)
    elif isinstance(output, tuple):
        return tuple(
            quantizer(tensor)
            for tensor in output
            if tensor.dtype in [to.float32, to.complex64]
        )
    return output
