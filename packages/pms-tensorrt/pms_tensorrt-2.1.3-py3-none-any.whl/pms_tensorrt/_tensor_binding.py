from pms_tensorrt._const import *
from pms_tensorrt._tensor_mode import TensorMode
from pms_tensorrt._utils import (
    mem_alloc_pagelocked,
    mem_alloc_device,
    mem_release_device,
    mem_release_pagelocked,
    set_context_tensor_address,
    mem_copy_htod,
    mem_copy_dtoh,
)
import tensorrt as trt


@dataclass
class TensorBinding:

    def __init__(self, engine: Any, context: Any, binding_index: int):
        self._engine = engine
        self._context = context
        self._is_binded = False
        self.binding_index = binding_index
        self._device_ptr = -1
        self._host_handle = None
        self._device_ptr: int = -1
        self._host_buffer: np.ndarray | None = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.unbind()

    def __del__(self):
        try:
            self.unbind()
        except Exception:
            pass

    def bind(self, shape: list[int], dtype: np.dtype):
        assert self.is_binded == False, "ERROR, This instance already binded."
        if self.mode == TensorMode.INPUT:
            self._context.set_input_shape(self.name, shape)
        self._host_buffer = mem_alloc_pagelocked(shape=shape, dtype=dtype)
        self._device_ptr = mem_alloc_device(size=self._host_buffer.nbytes)
        set_context_tensor_address(self._context, self.name, self._device_ptr)
        self._is_binded = True

    def unbind(self):
        """TRT 바인딩 해제 + 디바이스/호스트 메모리 해제"""
        if not self._is_binded:
            return
        # 1) TRT 텐서 주소 분리
        try:
            set_context_tensor_address(self._context, self.name, 0)
        except Exception:
            pass
        # 2) 디바이스 메모리 free
        try:
            mem_release_device(self._device_ptr)
        except Exception:
            pass
        finally:
            self._device_ptr = -1
        # 3) pinned host free (numpy view → ptr로 해제)
        try:
            if self._host_buffer is not None:
                mem_release_pagelocked(self._host_buffer)
        except Exception:
            pass
        finally:
            self._host_buffer = None
            self._is_binded = False

    def upload(self):
        mem_copy_htod(
            host_memory=self.host_buffer,
            device_ptr=self.device_ptr,
        )

    def download(self):
        mem_copy_dtoh(
            device_ptr=self.device_ptr,
            host_memory=self.host_buffer,
        )

    @property
    def name(self) -> str:
        return self._engine.get_tensor_name(self.binding_index)

    @property
    def mode(self) -> TensorMode:
        return TensorMode(self._engine.get_tensor_mode(self.name).value)

    @property
    def dtype(self) -> np.dtype:
        dtype = self._engine.get_tensor_dtype(self.name)
        return np.dtype(trt.nptype(dtype))

    @property
    def org_shape(self) -> List[int]:
        org_shape = self._engine.get_tensor_shape(self.name)
        return org_shape

    @property
    def is_binded(self) -> bool:
        return self._is_binded

    @property
    def device_ptr(self) -> int:
        assert self.is_binded, "ERROR, This instance is not binded."
        return self._device_ptr

    @property
    def host_buffer(self) -> np.ndarray:
        assert self.is_binded, "ERROR, This instance is not binded."
        return self._host_buffer

    @property
    def host_ptr(self) -> int:
        assert self.is_binded, "ERROR, This instance is not binded."
        return self.host_buffer.ctypes.data
