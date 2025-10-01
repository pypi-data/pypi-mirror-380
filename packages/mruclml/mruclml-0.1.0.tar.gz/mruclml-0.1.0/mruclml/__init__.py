
import builtins  


_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}


_ART = r"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   __  __      _   _      _           _  ~
~  |  \/  |_ __| | | | ___| |_ __ ___ | | ~
~  | |\/| | '__| | | |/ __| | '_ ` _ \| | ~
~  | |  | | |  | |_| | (__| | | | | | | | ~
~  |_|  |_|_|   \___/ \___|_|_| |_| |_|_| ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def print(color="white"):

    if isinstance(color, str):
        c = _COLORS.get(color.lower(), _COLORS["white"])
        builtins.print(c + _ART + _COLORS["reset"])

    elif isinstance(color, (list, tuple)):
        lines = _ART.splitlines()
        for i, line in enumerate(lines):
            c = _COLORS.get(color[i % len(color)].lower(), _COLORS["white"])
            builtins.print(c + line + _COLORS["reset"])
    else:
        raise TypeError("color باید str یا list از str باشد.")