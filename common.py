import sys


def read_puzzle_input(file_path: str) -> list[str]:
    """Reads a puzzle input text file located in the root of the current directory.

    Args:
        Puzzle input file path

    Returns:
        Text file represented as a list of strings
    """

    try:
        with open(file=file_path, mode="r") as file:
            return [line.replace("\n", "") for line in file.readlines()]
    except FileNotFoundError as exception:
        sys.exit(
            f"{exception.__class__.__name__}: "
            f"Puzzle input text file is missing in the root of the day_XY/ directory"
        )
