# BAML Python API: provides the Python API for the BAML runtime.

__version__ = "0.208.5.10"
UPSTREAM_VERSION = "0.208.5"
UPSTREAM_COMMIT = "main"
PATCH_VERSION = "1"

# Re-export the pyo3 API
from .baml_py import (
    AbortController,
    BamlRuntime,
    FunctionResult,
    FunctionResultStream,
    BamlImagePy as Image,
    BamlAudioPy as Audio,
    invoke_runtime_cli,
    BamlPdfPy as Pdf,
    BamlVideoPy as Video,
    ClientRegistry,
    # Collector utilities
    Collector,
    FunctionLog,
    LLMCall,
    Timing,
    Usage,
    HTTPRequest,
)
from .stream import BamlStream, BamlSyncStream
from .ctx_manager import CtxManager as BamlCtxManager

__all__ = [
    "AbortController",
    "BamlRuntime",
    "ClientRegistry",
    "BamlStream",
    "BamlSyncStream",
    "BamlCtxManager",
    "FunctionResult",
    "FunctionResultStream",
    "Image",
    "Audio",
    "Pdf",
    "Video",
    "invoke_runtime_cli",
    # Collector types
    "Collector",
    "FunctionLog",
    "LLMCall",
    "Timing",
    "Usage",
    "HTTPRequest",
]
