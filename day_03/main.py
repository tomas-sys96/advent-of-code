from typing import Optional

PERIOD: str = "."


def read_file(filename: str) -> list[str]:
    """Reads a text file in the current directory and returns its contents as a list of strings.

    Args:
        filename: Name of the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=filename, mode="r") as file:
        return [line.replace("\n", "") for line in file.readlines()]


def is_horizontally_adjacent(start_index: int, stop_index: int, current_line: str) -> bool:
    """"""

    for index in (start_index, stop_index):
        sign: int = 1 if index == start_index else -1
        character: str = current_line[index + 1 * sign]
        if not (character.isdigit() and character == PERIOD):
            return True

    return False


def is_vertically_adjacent(
    start_index: int,
    stop_index: int,
    previous_line: Optional[str],
    next_line: Optional[str],
) -> bool:
    """"""

    for line in (previous_line, next_line):
        if not line:
            continue
        for index in range(start_index - 1, stop_index + 2):
            character: str = line[index]
            if not (character.isdigit() and character == PERIOD):
                return True

    return False


def is_number_adjacent_to_symbol(
    start_index: int,
    stop_index: int,
    current_line: str,
    previous_line: Optional[str],
    next_line: Optional[str],
) -> bool:
    """"""

    # Horizontal check
    if is_horizontally_adjacent(
        start_index=start_index,
        stop_index=stop_index,
        current_line=current_line,
    ):
        return True

    # Vertical/diagonal check
    if is_vertically_adjacent(
        start_index=start_index,
        stop_index=stop_index,
        previous_line=previous_line,
        next_line=next_line,
    ):
        return True

    return False


def main() -> None:
    """"""

    lines: list[str] = read_file(filename="puzzle_input.txt")

    digits: list[str] = []

    for line_index, line in enumerate(lines):
        for character_index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
            if not line[character_index + 1].isdigit() and digits:
                start_index: int = character_index - (len(digits) - 1)
                current_line: str = line
                previous_line: Optional[str] = None
                next_line: Optional[str] = None

                # Will fail for the first line
                try:
                    previous_line = lines[line_index - 1]
                except IndexError:
                    pass

                # Will fail for the last line
                try:
                    next_line = lines[line_index + 1]
                except IndexError:
                    pass

                if is_number_adjacent_to_symbol(
                    start_index=start_index,
                    stop_index=character_index,
                    current_line=current_line,
                    previous_line=previous_line,
                    next_line=next_line,
                ):
                    pass

                digits = []


if __name__ == "__main__":
    main()
