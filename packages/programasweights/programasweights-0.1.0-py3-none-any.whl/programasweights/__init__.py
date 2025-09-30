__all__ = ["__version__"]

__version__ = "0.1.0"

def __getattr__(name):
    """Block access to all functionality - package is not ready yet."""
    if name == "function":
        raise NotImplementedError(
            "ProgramAsWeights is not yet ready for public use. "
            "This package is currently a placeholder to reserve the name. "
            "Please check back later for updates."
        )
    raise AttributeError(f"module 'programasweights' has no attribute '{name}'") 