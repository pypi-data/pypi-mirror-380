import cmath as _cmath
from typing import Tuple

e = _cmath.e
pi = _cmath.pi

def phase(z: complex) -> float:
    """Phase of z in radians, for instance phase(1j)=1.570796326794897.

    Args:
        z (complex): A complex number.

    Returns:
        float: Phase of `z` in radians, between -pi and pi.
    """
    return _cmath.phase(z)

def polar(z: complex) -> Tuple[float, float]:
    """Representation of z in polar coordinates: polar(1j) returns (1.0, 1.570796326794897).

    Args:
        z (complex): A complex number.

    Returns:
        float:  Tuple[float, float]: (modulus, phase)
    """    
    return _cmath.polar(z)

def rect(r: float, phi: float) -> complex:
    """Representation of a complex number in cartesian coordinates.

    Args:
        r (float): Modulus (distance from origin)
        phi (float): Angle in radians

    Returns:
        complex: Complex number in cartesian form
    """    
    return _cmath.rect(r, phi)

def exp(x: complex) -> complex:
    """Exponential function of x.

    Args:
        x (complex): Exponent

    Returns:
        complex: e ** x
    """    
    return _cmath.exp(x)


def log(x: complex) -> complex:
    """Natural logarithm of x.

    Args:
        x (complex): Complex number

    Returns:
        complex: Natural logarithm of x
    """    
    return _cmath.log(x)

def sqrt(x: complex) -> complex:
    """Square root of x.

    Returns the principal square root of x.
    
    Args:
        x (complex): Complex number

    Returns:
        complex: Square root of x
    """
    return _cmath.sqrt(x)

def cos(x: complex) -> complex:
    """Cosine of x (in radians).

    Args:
        x (complex): Complex number in radians

    Returns:
        complex: Cosine of x
    """
    return _cmath.cos(x)

def sin(x: complex) -> complex:
    """Sine of x (in radians).

    Args:
        x (complex): Complex number in radians

    Returns:
        complex: Sine of x
    """
    return _cmath.sin(x)

__all__ = [
    "e", "pi", "phase", "polar", "rect", "exp", "log", "sqrt", "cos", "sin"
]