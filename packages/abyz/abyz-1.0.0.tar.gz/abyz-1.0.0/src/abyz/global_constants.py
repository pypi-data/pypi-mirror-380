import sys
import pathlib

ABYZ_SRC_PATH = str(pathlib.Path(__file__).parent.resolve())

if sys.platform=="win32":
    SINGLES_PATH = ABYZ_SRC_PATH + r"\reserved\keywords.json"
    NUMBERS_PATH = ABYZ_SRC_PATH + r"\reserved\numbers.json"
else:
    SINGLES_PATH = ABYZ_SRC_PATH + "/reserved/keywords.json"
    NUMBERS_PATH = ABYZ_SRC_PATH + "/reserved/numbers.json"
