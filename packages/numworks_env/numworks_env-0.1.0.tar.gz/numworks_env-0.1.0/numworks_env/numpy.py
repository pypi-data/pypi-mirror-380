from typing import List, Tuple, Union
import numpy as _numpy
from numpy.typing import ArrayLike, NDArray


def array(lst: List) -> NDArray:
    """Creates an array from a list.

    Args:
        lst (List): Input list of numbers or nested lists.

    Returns:
        NDArray: NumPy array created from the given list.
    """
    return _numpy.array(lst)


def arange(start: int, stop: int) -> NDArray:
    """Returns an array of integers from start to stop-1.

    Args:
        start (int): Starting value.
        stop (int): End value (exclusive).

    Returns:
        NDArray: Array of integers.
    """
    return _numpy.arange(start, stop)


def concatenate(a: Tuple[ArrayLike, ArrayLike]) -> NDArray:
    """Returns an array that joins array b to array a.

    Args:
        a (Tuple[ArrayLike, ArrayLike]): Two arrays to concatenate.

    Returns:
        NDArray: Concatenated array.
    """
    return _numpy.concatenate(a)


def linspace(start: float, stop: float, n: int) -> NDArray:
    """Returns an array of n values evenly spaced over the specified interval.

    Args:
        start (float): Start value.
        stop (float): Stop value.
        n (int): Number of samples.

    Returns:
        NDArray: Evenly spaced values.
    """
    return _numpy.linspace(start, stop, n)


def ones(n: int) -> NDArray:
    """Returns an array of size n filled with ones.

    Args:
        n (int): Size of the array.

    Returns:
        NDArray: Array filled with ones.
    """
    return _numpy.ones(n)


def zeros(n: int) -> NDArray:
    """Returns an array of size n filled with zeros.

    Args:
        n (int): Size of the array.

    Returns:
        NDArray: Array filled with zeros.
    """
    return _numpy.zeros(n)


def flatten(a: ArrayLike) -> NDArray:
    """Returns a copy of an array collapsed into one dimension.

    Args:
        a (ArrayLike): Input array.

    Returns:
        NDArray: Flattened array.
    """
    return _numpy.array(a).flatten()


def reshape(a: ArrayLike, shape: Tuple[int, int]) -> NDArray:
    """Transforms an array to an array of size (n,m).

    Args:
        a (ArrayLike): Input array.
        shape (Tuple[int, int]): Desired shape (rows, columns).

    Returns:
        NDArray: Reshaped array.
    """
    return _numpy.array(a).reshape(shape)


def shape(a: ArrayLike) -> Tuple[int, ...]:
    """Returns the size of the array in the form (n,m).

    Args:
        a (ArrayLike): Input array.

    Returns:
        Tuple[int, ...]: Shape of the array.
    """
    return _numpy.array(a).shape


def tolist(a: ArrayLike) -> List:
    """Converts an array into a list.

    Args:
        a (ArrayLike): Input array.

    Returns:
        List: Converted list.
    """
    return _numpy.array(a).tolist()


def transpose(a: ArrayLike) -> NDArray:
    """Returns a transposed array.

    Args:
        a (ArrayLike): Input array.

    Returns:
        NDArray: Transposed array.
    """
    return _numpy.transpose(a)


def argmax(a: ArrayLike) -> int:
    """Returns the indices of the maximum values.

    Args:
        a (ArrayLike): Input array.

    Returns:
        int: Index of the maximum value.
    """
    return _numpy.argmax(a)


def argmin(a: ArrayLike) -> int:
    """Returns the indices of the minimum values.

    Args:
        a (ArrayLike): Input array.

    Returns:
        int: Index of the minimum value.
    """
    return _numpy.argmin(a)


def dot(a: ArrayLike, b: ArrayLike) -> NDArray:
    """Returns the dot product of two arrays.

    Args:
        a (ArrayLike): First array.
        b (ArrayLike): Second array.

    Returns:
        NDArray: Dot product.
    """
    return _numpy.dot(a, b)


def cross(a: ArrayLike, b: ArrayLike) -> NDArray:
    """Returns the cross product of two arrays.

    Args:
        a (ArrayLike): First array.
        b (ArrayLike): Second array.

    Returns:
        NDArray: Cross product.
    """
    return _numpy.cross(a, b)


def max(a: ArrayLike) -> Union[int, float]:
    """Returns the maximum of the elements.

    Args:
        a (ArrayLike): Input array.

    Returns:
        Union[int, float]: Maximum value.
    """
    return _numpy.max(a)


def min(a: ArrayLike) -> Union[int, float]:
    """Returns the minimum of the elements.

    Args:
        a (ArrayLike): Input array.

    Returns:
        Union[int, float]: Minimum value.
    """
    return _numpy.min(a)


def mean(a: ArrayLike) -> float:
    """Returns the mean of the elements.

    Args:
        a (ArrayLike): Input array.

    Returns:
        float: Mean value.
    """
    return _numpy.mean(a)


def median(a: ArrayLike) -> float:
    """Returns the median of the elements.

    Args:
        a (ArrayLike): Input array.

    Returns:
        float: Median value.
    """
    return _numpy.median(a)


def polyfit(x: ArrayLike, y: ArrayLike, d: int) -> NDArray:
    """Fits a polynomial regression of degree d to the points (x,y).

    Returns a vector of coefficients that minimizes the squared error
    in the order d, d-1, …, 0.

    Args:
        x (ArrayLike): x values.
        y (ArrayLike): y values.
        d (int): Degree of the polynomial.

    Returns:
        NDArray: Polynomial coefficients.
    """
    return _numpy.polyfit(x, y, d)


def polyval(p: ArrayLike, x: ArrayLike) -> NDArray:
    """Evaluates the polynomial p at x.

    Args:
        p (ArrayLike): Polynomial coefficients.
        x (ArrayLike): Values at which to evaluate.

    Returns:
        NDArray: Evaluated values.
    """
    return _numpy.polyval(p, x)


def size(a: ArrayLike) -> int:
    """Returns the number of elements in the array.

    Args:
        a (ArrayLike): Input array.

    Returns:
        int: Number of elements.
    """
    return _numpy.size(a)


def sort(a: ArrayLike) -> NDArray:
    """Sorts the array in ascending order.

    Args:
        a (ArrayLike): Input array.

    Returns:
        NDArray: Sorted array.
    """
    return _numpy.sort(a)


def std(a: ArrayLike) -> float:
    """Returns the standard deviation of the elements.

    Args:
        a (ArrayLike): Input array.

    Returns:
        float: Standard deviation.
    """
    return _numpy.std(a)


def sum(a: ArrayLike) -> Union[int, float]:
    """Returns the sum of the elements.

    Args:
        a (ArrayLike): Input array.

    Returns:
        Union[int, float]: Sum of elements.
    """
    return _numpy.sum(a)
