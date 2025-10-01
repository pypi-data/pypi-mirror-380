from typing import Union


Number = Union[int, float]


def logAccuracy(accuracy: Number) -> None:
    """Stub for logging accuracy.

    Args:
        accuracy: Classification accuracy for the current step.
    """

    # No-op stub. Will be implemented to send metrics to log.
    return None


__all__ = ["logAccuracy"]
__version__ = "0.0.1"


