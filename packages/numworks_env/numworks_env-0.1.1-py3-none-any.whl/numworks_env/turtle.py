from typing import Tuple, Union
import turtle as _turtle
import sys

_t: _turtle.Turtle = None
_screen: _turtle.Screen = None

def init(width: int = 320, height: int = 240, title: str = "NumWorks Turtle") -> None:
    global _t, _screen
    _screen = _turtle.Screen()
    _screen.setup(width=width, height=height)
    _screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", sys.exit)
    _screen.title(title)
    _t = _turtle.Turtle()
    
def forward(x: float) -> None:
    """Move forward by x pixels

    Args:
        x (float): Distance to move forward.
    """    
    _t.forward(x)
    
def backward(x: float) -> None:
    """Move backward by x pixels

    Args:
        x (float): Distance to move backward.
    """    
    _t.backward(x)
    
def right(a: float) -> None:
    """Turn right by a degrees.

    Args:
        a (float): Angle in degrees to turn clockwise.
    """    
    _t.right(a)

def left(a: float) -> None:
    """Turn left by a degrees.

    Args:
        a (float): Angle in degrees to turn clockwise.
    """    
    _t.left(a)
    
def goto(x: float, y: float) -> None:
    """Move to (x, y) coordinates.

    Args:
        x (float): X-coordinate.
        y (float): Y-coordinate.
    """    
    _t.goto(x, y)

def setheading(a: float) -> None:
    """Set the orientation by a degrees.

    Args:
        a (float): Angle in degrees
    """    
    _t.setheading(a)

def circle(r: float) -> None:
    """Circle of radius r pixels.

    Args:
        r (float): Radius of the circle in pixels.
    """    
    _t.circle(r)

def speed(x: int) -> None:
    """Drawing speed (x between 0 and 10).

    Args:
        x (int): Speed from fastest to slowest
    """    
    _t.speed(x)
    
def position() -> Tuple[float, float]:
    """Return the current (x,y) location.

    Returns:
        Tuple[float, float]: Current (x, y) coordinates.
    """    
    return _t.position()

def heading() -> float:
    """Return the current heading.

    Returns:
        float: Current heading in degrees.
    """    
    return _t.heading()

def pendown() -> None:
    """Pull the pen down."""    
    _t.pendown()

def penup() -> None:
    """Pull the pen up."""    
    _t.penup()
    
def pensize(x: int) -> None:
    """Set the line thickness to x pixels.

    Args:
        x (int): Pen thickness in pixels.
    """    
    _t.pensize(x)

def write(text: str) -> None:
    """Writes the text placed as an argument at the position of the turtle.

    Args:
        text (str): Text string to display.
    """    
    _t.write(text)

def isdown() -> bool:
    """Return True if the pen is down.

    Returns:
        bool: True if the pen is down, False otherwise.
    """    
    return _t.isdown()

def reset() -> None:
    """Reset the drawing."""
    _t.reset()

def showturtle() -> None:
    """Show the turtle"""
    _t.showturtle()

def hideturtle() -> None:
    """Hide the turtle."""
    _t.hideturtle()
    
def color(c: Union[str, Tuple[int, int, int]]) -> None:
    """Set the pen color.

    Args:
        c (Union[str, Tuple[int, int, int]]): Color name or RGB tuple (0-255).
    """    
    _t.color(c)

def colormode(x: Union[int, float]) -> None:
    """Set the color mode for RGB tuples used in `color()`.

    Args:
        x (int | float): 
            - 1.0 → colors must be specified as floats in the range [0.0, 1.0], e.g., (0.5, 1.0, 0.5)
            - 255 → colors must be specified as integers in the range [0, 255], e.g., (128, 255, 128)
            By default, the color mode is 255.
    """
    _turtle.colormode(x)

def done() -> None:
    """Keep the Turtle window open until manually closed."""
    if _screen:
        _turtle.done()

blue = "blue"
red = "red"
green = "green"
yellow = "yellow"
brown = "brown"
black = "black"
white = "white"
pink = "pink"
orange = "orange"
purple = "purple"
grey = "grey"

__all__ = [
    "forward", "backward", "right", "left", "goto", "setheading",
    "circle", "speed", "position", "heading", "pendown", "penup",
    "pensize", "write", "isdown", "reset", "showturtle", "hideturtle",
    "color", "colormode", "blue", "red", "green", "yellow", "brown", "black", "white", "pink", "orange", "purple", "grey"
]