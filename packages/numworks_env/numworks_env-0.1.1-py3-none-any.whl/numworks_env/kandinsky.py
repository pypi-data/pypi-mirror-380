import tkinter as tk
from typing import Tuple, Union, Optional
import sys 

_root: Optional[tk.Tk] = None
_canvas: Optional[tk.Canvas] = None
_pixels = {}

def init(width: int = 320, height: int = 240, title: str = "Kandinsky") -> None:
    global _root, _canvas
    _root = tk.Tk()
    _root.title(title)
    _canvas = tk.Canvas(_root, width=width, height=height, bg="black")
    _canvas.winfo_toplevel().protocol("WM_DELETE_WINDOW", sys.exit)
    _canvas.pack()



_current_color = (0, 0, 0)


def color(
    r: Union[int, float, Tuple[int, int, int]], g: int = 0, b: int = 0
) -> Tuple[int, int, int]:
    """Defines the color from the values of r,g,b.

    Args:
        r (Union[int, float, Tuple[int, int, int]]): Red component or full color tuple
        g (int, optional): Green component. Defaults to 0.
        b (int, optional): Blue component. Defaults to 0.

    Returns:
        Tuple[int, int, int]: Color tuple.
    """
    global _current_color
    if isinstance(r, tuple):
        _current_color = r
    else:
        _current_color = (r, g, b)
    return _current_color


def get_pixel(x: int, y: int) -> Tuple[int, int, int]:
    """Returns the pixel x,y color as a tuple (r,g,b).

    Args:
        x (int): X-coordinate
        y (int): Y-coordinate

    Returns:
        Tuple[int, int, int]: Pixel at that location
    """
    return _pixels.get((x, y), (0, 0, 0))


def set_pixel(x: int, y: int, col: Tuple[int, int, int] = None) -> None:
    """Colors the pixel x,y of the color color.

    Args:
        x (int): X-coordinate
        y (int): Y-coordinate
        color (Tuple[int, int, int], optional): Color tuple. Defaults to current color.
    """
    if col is None:
        col = _current_color
    hex_color = "#%02x%02x%02x" % col
    _pixels[(x, y)] = col
    _canvas.create_line(x, y, x + 1, y, fill=hex_color)


def draw_string(
    text: str,
    x: int,
    y: int,
    col1: Tuple[int, int, int] = (255, 255, 255),
    col2: Tuple[int, int, int] = None,
) -> None:
    """
    Displays text from the pixel x,y

    Args:
        text (str): Text to display
        x (int): X-coordinate
        y (int): Y-coordinate
        col1 (tuple[int,int,int], optional): Foreground pixel. Defaults to white.
        col2 (tuple[int,int,int], optional): Background pixel. Defaults to None (transparent).
    """

    # cant really put a background using tkinter but might find a way for it!
    fg = "#%02x%02x%02x" % col1
    if col2:
        bg = "#%02x%02x%02x" % col2
    else:
        bg = ""
    _canvas.create_text(x, y, text=text, fill=fg, anchor="nw", font=("Arial", 12))


def fill_rect(
    x: int, y: int, width: int, height: int, pixel: Tuple[int, int, int]
) -> None:
    """
    Fills a rectangle at pixel (x,y) with the color color.

    Args:
        x (int): X-coordinate
        y (int): Y-coordinate
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        pixel (tuple[int,int,int]): Pixel color
    """
    hex_color = "#%02x%02x%02x" % pixel
    _canvas.create_rectangle(
        x, y, x + width, y + height, outline=hex_color, fill=hex_color
    )
    for i in range(x, x + width):
        for j in range(y, y + height):
            _pixels[(i, j)] = pixel

def done() -> None:
    """Start the Tkinter main loop to keep the window open."""
    if _root:
        _root.mainloop()