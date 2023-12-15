from dataclasses import dataclass
from typing import Optional


@dataclass
class Number:
    value: int
    start_index: int
    stop_index: int
    line_index: int
    line: str
    previous_line: Optional[str]
    next_line: Optional[str]


def read_file(file_path: str) -> list[str]:
    """Reads a text file and returns its contents as a list of strings.

    Args:
        file_path: Path to the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=file_path, mode="r") as file:
        return [line.replace("\n", "") for line in file.readlines()]


def get_adjacent_lines(line_index: int, lines: list[str]) -> tuple[Optional[str], Optional[str]]:
    """Get the previous and next line for a line at given index.

    Args:
        line_index: Index of the line
        lines: List of lines

    Returns:
        tuple:
            previous_line: Line before the given line,
            next_line: Line after the given line
    """

    # There's no "previous"/"next" line for the first/last line
    previous_line: Optional[str] = lines[line_index - 1] if line_index != 0 else None
    next_line: Optional[str] = lines[line_index + 1] if line_index != (len(lines) - 1) else None

    return previous_line, next_line
