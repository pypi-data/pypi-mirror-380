__all__ = ["function", "compile", "compile_dummy", "__version__"]

__version__ = "0.1.1"
 
from .runtime import function  # noqa: E402
from .compiler import compile, compile_dummy  # noqa: E402 