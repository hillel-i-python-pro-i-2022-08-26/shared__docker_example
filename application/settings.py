import pathlib
from typing import Final

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
INPUT_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath("input")
