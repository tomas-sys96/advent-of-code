import sys

PATH_TO_PUZZLE_INPUT: str = "../puzzle_input.txt"


def read_puzzle_input() -> list[str]:
    """Reads a puzzle input text file located in the root of the current directory.

    Returns:
        Text file represented as a list of strings
    """

    try:
        with open(file=PATH_TO_PUZZLE_INPUT, mode="r") as file:
            return [line.replace("\n", "") for line in file.readlines()]
    except FileNotFoundError as exception:
        sys.exit(
            f"{exception.__class__.__name__}: "
            f"Puzzle input text file is missing in the root of the day_xy/ directory"
        )
