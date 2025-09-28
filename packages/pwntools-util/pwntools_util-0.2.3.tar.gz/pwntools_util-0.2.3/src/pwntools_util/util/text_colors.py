# ----- text colors -----

# imports

from enum import Enum

# constants

class TextColorCodes(Enum):
    Black = '\033[90m'
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Purple = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Reset = '\033[0m'

# functions

def colorize(text: str, color: TextColorCodes):
    return color.value + text + TextColorCodes.Reset.value
