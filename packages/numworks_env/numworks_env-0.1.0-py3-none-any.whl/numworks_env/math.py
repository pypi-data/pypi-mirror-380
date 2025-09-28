import math as _math
from typing import Tuple

e = _math.e
pi = _math.pi 

def sqrt(x: float) -> float:
    """Square root, type sqrt(x) for √x.

    Args:
        x (float): A non-negative number.

    Returns:
        float: The square root of x.
    """    
    return _math.sqrt(x)

def pow(x: float, y: float) -> float:
    """Power, type pow(x,y) for x ** y.

    Args:
        x (float): Base
        y (float): Exponent

    Returns:
        float:  x ** y.
    """    
    return _math.pow(x, y)

def exp(x: float) -> float:
    """Exponential, type exp(x) for e ** x.

    Args:
        x (float): Exponent

    Returns:
        float: e ** x
    """    
    return _math.exp(x)

def expm1(x: float) -> float:
    """Exponential, type exp(x) for e ** x - 1.

    Args:
        x (float): Exponent

    Returns:
        float: e ** x - 1
    """    
    return _math.exp(x)

def log(x: float) -> float:
    """Natural logarithm: log(x) calculates ln(x).

    Args:
        x (float): Positive number.

    Returns:
        float: ln(x)
    """    
    return _math.log(x)


def log2(x: float) -> float:
    """Base-2 logarithm: log(x) calculates log2(x).

    Args:
        x (float): Positive number.

    Returns:
        float: log2(x).
    """    
    return _math.log2(x)


def log10(x: float) -> float:
    """Base-10 logarithm: log(x) calculates log10(x).

    Args:
        x (float): Positive number.

    Returns:
        float: log10(x).
    """    
    return _math.log10(x)

def cosh(x: float) -> float:
    """Return the hyperbolic cosine of x."""
    return _math.cosh(x)

def sinh(x: float) -> float:
    """Return the hyperbolic sine of x."""
    return _math.sinh(x)

def tanh(x: float) -> float:
    """Return the hyperbolic tangent of x."""
    return _math.tanh(x)

def acosh(x: float) -> float:
    """Return the inverse hyperbolic cosine of x."""
    return _math.acosh(x)

def asinh(x: float) -> float:
    """Return the inverse hyperbolic sine of x."""
    return _math.asinh(x)

def atanh(x: float) -> float:
    """Return the inverse hyperbolic tangent of x."""
    return _math.atanh(x)

def cos(x: float) -> float:
    """Return the cosine of x radians."""
    return _math.cos(x)

def sin(x: float) -> float:
    """Return the sine of x radians."""
    return _math.sin(x)

def tan(x: float) -> float:
    """Return the tangent of x radians."""
    return _math.tan(x)

def acos(x: float) -> float:
    """Return the arc cosine of x in radians."""
    return _math.acos(x)

def asin(x: float) -> float:
    """Return the arc sine of x in radians."""
    return _math.asin(x)

def atan(x: float) -> float:
    """Return the arc tangent of x in radians."""
    return _math.atan(x)

def atan2(y: float, x: float) -> float:
    """Return atan(y / x) in radians, taking into account the quadrant."""
    return _math.atan2(y, x)

def ceil(x: float) -> int:
    """Return the ceiling of x as an int."""
    return _math.ceil(x)

def floor(x: float) -> int:
    """Return the floor of x as an int."""
    return _math.floor(x)

def trunc(x: float) -> int:
    """Return the integer part of x, truncated towards 0."""
    return _math.trunc(x)

def fabs(x: float) -> float:
    """Return the absolute value of x."""
    return _math.fabs(x)

def copysign(x: float, y: float) -> float:
    """Return x with the sign of y."""
    return _math.copysign(x, y)


def fmod(a: float, b: float) -> float:
    """Return the remainder of a / b."""
    return _math.fmod(a, b)

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b."""
    return _math.gcd(a, b)

def frexp(x: float) -> Tuple[float,int]:
    """Return the mantissa and exponent of x such that x = mantissa * 2**exponent."""
    return _math.frexp(x)

def ldexp(x: float, i: int) -> float:
    """Return x * (2 ** i)."""
    return _math.ldexp(x, i)

def modf(x: float) -> Tuple[float,float]:
    """Return the fractional and integer parts of x."""
    return _math.modf(x)

def isfinite(x: float) -> bool:
    """Return True if x is finite."""
    return _math.isfinite(x)

def isinf(x: float) -> bool:
    """Return True if x is infinite."""
    return _math.isinf(x)

def isnan(x: float) -> bool:
    """Return True if x is NaN."""
    return _math.isnan(x)

# Conversion
def radians(x: float) -> float:
    """Convert x from degrees to radians."""
    return _math.radians(x)

def degrees(x: float) -> float:
    """Convert x from radians to degrees."""
    return _math.degrees(x)

def erf(x: float) -> float:
    """Return the error function at x."""
    return _math.erf(x)

def erfc(x: float) -> float:
    """Return the complementary error function at x."""
    return _math.erfc(x)

def gamma(x: float) -> float:
    """Return the gamma function at x."""
    return _math.gamma(x)

def lgamma(x: float) -> float:
    """Return the natural logarithm of the absolute value of the gamma function at x."""
    return _math.lgamma(x)

__all__ = [
    "e", "pi", "sqrt", "pow", "exp", "expm1", "log", "log2", "log10",
    "cos", "sin", "tan", "acos", "asin", "atan", "atan2",
    "cosh", "sinh", "tanh", "acosh", "asinh", "atanh",
    "ceil", "floor", "trunc", "fabs", "copysign",
    "fmod", "gcd", "frexp", "ldexp", "modf",
    "isfinite", "isinf", "isnan",
    "radians", "degrees",
    "erf", "erfc", "gamma", "lgamma"
]