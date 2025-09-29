import matplotlib.pyplot as _pyplot
from typing import List, Union, Tuple

_fig, _ax = _pyplot.subplots()

def arrow(x: float, y: float, dx: float, dy: float, head_width: float = 0.05, color: str = "black") -> None:
    """
    Draws an arrow from (x, y) to (x+dx, y+dy).

    Args:
        x (float): Starting x-coordinate.
        y (float): Starting y-coordinate.
        dx (float): Change in x (arrow length along x).
        dy (float): Change in y (arrow length along y).
        head_width (float, optional): Width of the arrow head. Defaults to 0.05.
        color (str, optional): Color of the arrow. Defaults to "black".
    """
    _ax.arrow(x, y, dx, dy, head_width=head_width, color=color)

def axis(bounds: Union[Tuple[float, float, float, float], str, bool]) -> None:
    """
    Sets the display window or controls the axes visibility.

    - `axis((xmin, xmax, ymin, ymax))` sets the axes limits.
    - `axis("on")` or `axis(True)` shows the axes.
    - `axis("off")` or `axis(False)` hides the axes.
    - `axis("auto")` resets axes to automatic limits.

    Args:
        bounds (tuple[str, bool]): A 4-tuple (xmin, xmax, ymin, ymax), a string "on"/"off"/"auto",
                                   or a boolean True/False to show/hide axes.
    """
    if bounds in ["on", True]:
        _ax.axis("on")
    elif bounds in ["off", False]:
        _ax.axis("off")
    elif bounds == "auto":
        _ax.axis("auto")
    else:
        _ax.axis(bounds)

def bar(x: List[float], height: List[float], bin_width: float = 0.8, bottom: float = 0, color: str = "black") -> None:
    """
    Draws a bar plot.

    Args:
        x (List[float]): x-coordinates of the bars.
        height (List[float]): Heights of the bars.
        bin_width (float, optional): Width of each bar. Defaults to 0.8.
        bottom (float, optional): Bottom y-value. Defaults to 0.
        color (str, optional): Bar color. Defaults to "black".
    """
    _ax.bar(x, height, width=bin_width, bottom=bottom, color=color)

def grid(on: bool = True) -> None:
    """
    Displays the grid if it is hidden or hides the grid if it is displayed.

    Args:
        on (bool, optional): True to show grid, False to hide. Defaults to True.
    """
    _ax.grid(on)
    
def hist(x: List[float], bins: Union[int, List[float]] = 10, color: str = "black") -> None:
    """
    Plots a histogram using the values in the x list.

    Args:
        x (List[float]): Data to bin.
        bins (int or List[float], optional): Number of bins or bin edges. Defaults to 10.
        color (str, optional): Color of the bars. Defaults to "black".
    """
    _ax.hist(x, bins=bins, color=color)

def plot(x: List[float], y: List[float] = None, color: str = "black") -> None:
    """
    Plots the y list versus the x list

    Args:
        x (List[float]): x-coordinates or y-values if y is None.
        y (List[float], optional): y-coordinates. Defaults to None.
        color (str, optional): Line color. Defaults to "black".
    """
    if y is None:
        y = x
        x = list(range(len(y)))
    _ax.plot(x, y, color=color)
    
def scatter(x: List[float], y: List[float], color: str = "black") -> None:
    """
    Plots the y list versus the x list

    Args:
        x (List[float]): x-coordinates.
        y (List[float]): y-coordinates.
        color (str, optional): Point color. Defaults to "black".
    """
    _ax.scatter(x, y, color=color)
    
def show() -> None:
    """
    Display the figure.
    """
    _pyplot.show()

def text(x: float, y: float, string: str, color: str = "black") -> None:
    """
    Displays the text set as an argument at the (x,y) coordinates.

    Args:
        x (float): x-coordinate.
        y (float): y-coordinate.
        string (str): Text to display.
        color (str, optional): Text color. Defaults to "black".
    """
    _ax.text(x, y, string, color=color)

