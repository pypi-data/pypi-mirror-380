from collections.abc import Callable, Mapping, Sequence
import enum
from typing import Annotated

from numpy.typing import NDArray


ORT_API_VERSION: int = 23

class HardwareDeviceType(enum.Enum):
    CPU = 0

    GPU = 1

    NPU = 2

class ExecutionProviderDevicePolicy(enum.Enum):
    DEFAULT = 0

    PREFER_CPU = 1

    PREFER_NPU = 2

    PREFER_GPU = 3

    MAX_PERFORMANCE = 4

    MAX_EFFICIENCY = 5

    MIN_OVERALL_POWER = 6

class HardwareDevice:
    @property
    def type(self) -> HardwareDeviceType: ...

    @property
    def vendor_id(self) -> int: ...

    @property
    def vendor(self) -> str: ...

    @property
    def device_id(self) -> int: ...

    @property
    def metadata(self) -> dict[str, str]: ...

class EpDevice:
    @property
    def ep_name(self) -> str: ...

    @property
    def ep_vendor(self) -> str: ...

    @property
    def ep_metadata(self) -> dict[str, str]: ...

    @property
    def ep_options(self) -> dict[str, str]: ...

    @property
    def device(self) -> HardwareDevice: ...

def register_execution_provider_library(arg0: str, arg1: str, /) -> None: ...

def unregister_execution_provider_library(arg: str, /) -> None: ...

def get_ep_devices() -> list[EpDevice]: ...

class ModelCompilationOptions:
    def set_input_model_path(self, path: str) -> None: ...

    def set_input_model_from_buffer(self, model_bytes: bytes) -> None: ...

    def set_output_model_external_initializers_file(self, path: str, external_initializer_size_threshold: int) -> None: ...

    def set_ep_context_embed_mode(self, embed_context: bool) -> None: ...

    def compile_model_to_file(self, path: str) -> None: ...

    def compile_model_to_buffer(self) -> bytes: ...

class SessionOptions:
    def __init__(self) -> None: ...

    def append_execution_provider_v2(self, ep_devices: Sequence[EpDevice], options: Mapping[str, str]) -> None: ...

    def set_ep_selection_policy(self, policy: ExecutionProviderDevicePolicy) -> None: ...

    def set_ep_selection_policy_delegate(self, delegate: Callable[[Sequence[EpDevice], Mapping[str, str], Mapping[str, str], int], Sequence[EpDevice]]) -> None: ...

    def create_model_compilation_options(self) -> ModelCompilationOptions: ...

class TensorInfo:
    @property
    def shape(self) -> list[int]: ...

    @property
    def dimensions(self) -> list[str]: ...

    @property
    def dtype(self) -> str: ...

class Session:
    def __init__(self, model_path: str, options: SessionOptions) -> None: ...

    def get_input_info(self) -> dict[str, TensorInfo]: ...

    def get_output_info(self) -> dict[str, TensorInfo]: ...

    def run(self, inputs: Mapping[str, Annotated[NDArray, dict(order='C', device='cpu')]]) -> dict[str, Annotated[NDArray, dict(order='C', device='cpu')]]: ...
