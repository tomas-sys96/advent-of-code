from dataclasses import dataclass
from typing import Optional


@dataclass
class Number:
    value: int
    start_index: int
    stop_index: int
    line_index: int
    line: str
    previous_line: Optional[str] = None
    next_line: Optional[str] = None


@dataclass
class Symbol:
    index: int
    line_index: int
    line: str


def read_file(file_path: str) -> list[str]:
    """Reads a text file and returns its contents as a list of strings.

    Args:
        file_path: Path to the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=file_path, mode="r") as file:
        return [line.replace("\n", "") for line in file.readlines()]
