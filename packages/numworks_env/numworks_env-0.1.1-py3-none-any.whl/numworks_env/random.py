
from typing import List, Any
import random as _random;

def getrandbits(k: int) -> int:
    """Returns an integer with k random bits.

    Args:
        k (int): Number of random bits to generate. Must be a non-negative integer.

    Returns:
        int: An integer in the range [0, 2**k), i.e., with k bits of randomness.
    """    
    return _random.getrandbits(k)

def seed(x: int) -> None:
    """Initialize the random number generator.

    Args:
        x (int): Seed value to initialize the generator.
    """    
    return _random.seed(x)

def randrange(start: int, stop: int = None) -> int:
    """Returns a random number in range(start,stop)

    Args:
        start (int): Start of range if stop is specified, else stop value
        stop (int, optional): End of range (exclusive). Defaults to None.

    Returns:
        int: Random integer in the specified range.
    """    
    return _random.randrange(start, stop)

def randint(a: int, b: int) -> int:
    """Returns an integer in [a,b].

    Args:
        a (int): Lower bound (inclusive).
        b (int): Upper bound (inclusive).

    Returns:
        int: Random integer in [a, b].
    """    
    return _random.randint(a, b)

def choice(list: List[Any]) -> Any:
    """Returns a random number in the list.

    Args:
        list (List[Any]): Non-empty list to choose from.

    Raises:
        IndexError: If the list is empty.
        
    Returns:
        Any: Random element from the list.
    """    
    if not list:
        raise IndexError("Cannot choose from empty list")
    return _random.choice(list)

def random() -> float:
    """Returns a random floating point number in [0,1).

    Returns:
        float: A random float x such that 0 <= x < 1.
    """    
    return _random.random()

def uniform(a: float, b: float) -> float:
    """Returns a random floating point number in [a,b].

    Args:
        a (float): Lower bound of the range.
        b (float): Upper bound of the range.

    Returns:
        float: A random float x such that a <= x <= b.
    """    
    return _random.uniform(a, b)

__all__ = [
    "getrandbits",
    "seed",
    "randrange",
    "randint",
    "choice",
    "random",
    "uniform"
]