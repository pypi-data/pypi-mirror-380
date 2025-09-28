import time as _time;

def monotonic() -> float:
    """Returns the value of the clock at the time the function is called.
    """    
    return _time.monotonic()

def sleep(t: float) -> None:
    """Pauses execution for t seconds.

    Args:
        t (float): The number of seconds to pause execution
    """    
    _time.sleep(t)
    
__all__ = [
    "sleep",
    "monotonic"
]