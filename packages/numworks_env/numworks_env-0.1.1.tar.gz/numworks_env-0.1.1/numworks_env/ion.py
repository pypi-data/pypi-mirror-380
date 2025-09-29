from enum import IntEnum
import keyboard


class _Key(IntEnum):
    LEFT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    OK = 4
    BACK = 5
    HOME = 6
    ONOFF = 7
    SHIFT = 12
    ALPHA = 13
    XNT = 14
    VAR = 15
    TOOLBOX = 16
    BACKSPACE = 17
    EXP = 18
    LN = 19
    LOG = 20
    IMAGINARY = 21
    COMMA = 22
    POWER = 23
    SINE = 24
    COSINE = 25
    TANGENT = 26
    PI = 27
    SQRT = 28
    SQUARE = 29
    SEVEN = 30
    EIGHT = 31
    NINE = 32
    LEFTPARENTHESIS = 33
    RIGHTPARENTHESIS = 34
    FOUR = 36
    FIVE = 37
    SIX = 38
    MULTIPLICATION = 39
    DIVISION = 40
    ONE = 42
    TWO = 43
    THREE = 44
    PLUS = 45
    MINUS = 46
    ZERO = 48
    DOT = 49
    EE = 50
    ANS = 51
    EXE = 52

_KEYMAP = {
    _Key.LEFT: "left",
    _Key.UP: "up",
    _Key.DOWN: "down",
    _Key.RIGHT: "right",
    _Key.OK: "enter",
    _Key.BACK: "backspace",
    _Key.HOME: "home",
    _Key.ONOFF: "esc",
    _Key.SHIFT: "shift",
    _Key.ALPHA: "caps lock",
    _Key.XNT: "x",
    _Key.VAR: "v",
    _Key.TOOLBOX: "t",
    _Key.BACKSPACE: "backspace",
    _Key.EXP: "e",
    _Key.LN: "l",
    _Key.LOG: "g",
    _Key.IMAGINARY: "i",
    _Key.COMMA: ",",
    _Key.POWER: "^",
    _Key.SINE: "s",
    _Key.COSINE: "c",
    _Key.TANGENT: "t",
    _Key.PI: "p",
    _Key.SQRT: "r",
    _Key.SQUARE: "q",
    _Key.SEVEN: "7",
    _Key.EIGHT: "8",
    _Key.NINE: "9",
    _Key.LEFTPARENTHESIS: "(",
    _Key.RIGHTPARENTHESIS: ")",
    _Key.FOUR: "4",
    _Key.FIVE: "5",
    _Key.SIX: "6",
    _Key.MULTIPLICATION: "*",
    _Key.DIVISION: "/",
    _Key.ONE: "1",
    _Key.TWO: "2",
    _Key.THREE: "3",
    _Key.PLUS: "+",
    _Key.MINUS: "-",
    _Key.ZERO: "0",
    _Key.DOT: ".",
    _Key.EE: "e",
    _Key.ANS: "a",
    _Key.EXE: "enter",
}


def keydown(k: _Key) -> bool:
    """Returns True if the k key in argument is pressed and False otherwise.


    Args:
        k (Key): A key constant from the ion module


    Raises:
        ValueError: If the provided key constant is not recognized.


    Returns:
        bool: True if the corresponding computer key is pressed,
        False otherwise.
    """
    if not k in _KEYMAP:
        raise ValueError(f"Unknown key {k}")
    return keyboard.is_pressed(_KEYMAP[k])

KEY_LEFT = _Key.LEFT
KEY_UP = _Key.UP
KEY_DOWN = _Key.DOWN
KEY_RIGHT = _Key.RIGHT
KEY_OK = _Key.OK
KEY_BACK = _Key.BACK
KEY_HOME = _Key.HOME
KEY_ONOFF = _Key.ONOFF
KEY_SHIFT = _Key.SHIFT
KEY_ALPHA = _Key.ALPHA
KEY_XNT = _Key.XNT
KEY_VAR = _Key.VAR
KEY_TOOLBOX = _Key.TOOLBOX
KEY_BACKSPACE = _Key.BACKSPACE
KEY_EXP = _Key.EXP
KEY_LN = _Key.LN
KEY_LOG = _Key.LOG
KEY_IMAGINARY = _Key.IMAGINARY
KEY_COMMA = _Key.COMMA
KEY_POWER = _Key.POWER
KEY_SINE = _Key.SINE
KEY_COSINE = _Key.COSINE
KEY_TANGENT = _Key.TANGENT
KEY_PI = _Key.PI
KEY_SQRT = _Key.SQRT
KEY_SQUARE = _Key.SQUARE
KEY_SEVEN = _Key.SEVEN
KEY_EIGHT = _Key.EIGHT
KEY_NINE = _Key.NINE
KEY_LEFTPARENTHESIS = _Key.LEFTPARENTHESIS
KEY_RIGHTPARENTHESIS = _Key.RIGHTPARENTHESIS
KEY_FOUR = _Key.FOUR
KEY_FIVE = _Key.FIVE
KEY_SIX = _Key.SIX
KEY_MULTIPLICATION = _Key.MULTIPLICATION
KEY_DIVISION = _Key.DIVISION
KEY_ONE = _Key.ONE
KEY_TWO = _Key.TWO
KEY_THREE = _Key.THREE
KEY_PLUS = _Key.PLUS
KEY_MINUS = _Key.MINUS
KEY_ZERO = _Key.ZERO
KEY_DOT = _Key.DOT
KEY_EE = _Key.EE
KEY_ANS = _Key.ANS
KEY_EXE = _Key.EXE

__all__ = [
    "KEY_LEFT", "KEY_UP", "KEY_DOWN", "KEY_RIGHT",
    "KEY_OK", "KEY_BACK", "KEY_HOME", "KEY_ONOFF",
    "KEY_SHIFT", "KEY_ALPHA", "KEY_XNT", "KEY_VAR", "KEY_TOOLBOX",
    "KEY_BACKSPACE", "KEY_EXP", "KEY_LN", "KEY_LOG", "KEY_IMAGINARY",
    "KEY_COMMA", "KEY_POWER", "KEY_SINE", "KEY_COSINE", "KEY_TANGENT",
    "KEY_PI", "KEY_SQRT", "KEY_SQUARE",
    "KEY_SEVEN", "KEY_EIGHT", "KEY_NINE", "KEY_LEFTPARENTHESIS", "KEY_RIGHTPARENTHESIS",
    "KEY_FOUR", "KEY_FIVE", "KEY_SIX", "KEY_MULTIPLICATION", "KEY_DIVISION",
    "KEY_ONE", "KEY_TWO", "KEY_THREE", "KEY_PLUS", "KEY_MINUS",
    "KEY_ZERO", "KEY_DOT", "KEY_EE", "KEY_ANS", "KEY_EXE",
    "keydown"
]
