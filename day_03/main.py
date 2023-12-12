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


def is_symbol_at_index(line: str, index: int) -> bool:
    """Checks if a character at a given index is a valid symbol.

    Args:
        line: Line containing the character to be checked
        index: Index of the character on the line

    Returns:
        True if the character is a valid symbol, False otherwise
    """

    character: str = line[index]
    return not character.isdigit() and not character == PERIOD


def is_horizontally_adjacent_symbol(number_start_index: int, number_stop_index: int, current_line: str) -> bool:
    """Checks if there's a symbol adjacent to a number at given indices in the horizontal direction.

    Args:
        number_start_index: First index of the number on the current line
        number_stop_index: Last index of the number on the current line
        current_line: Line of the number being checked

    Returns:
        True if there's an adjacent symbol, False otherwise
    """

    for index in (number_start_index - 1, number_stop_index + 1):
        # Can be out of bounds if a digit is the first/last element on the line
        if index < 0 or index > (len(current_line) - 1):
            continue

        if is_symbol_at_index(line=current_line, index=index):
            return True

    return False


def is_vertically_adjacent_symbol(
    number_start_index: int,
    number_stop_index: int,
    previous_line: Optional[str],
    next_line: Optional[str],
) -> bool:
    """Checks if there's a symbol adjacent to a number at given indices in the vertical/diagonal direction.

    Args:
        number_start_index: First index of the number on the current line
        number_stop_index: Last index of the number on the current line
        previous_line: Line before the current line
        next_line: Line after the current line

    Returns:
        True if there's an adjacent symbol, False otherwise
    """

    for line in (previous_line, next_line):
        # A previous/next line may not exist -> skip to the next iteration
        if not line:
            continue
        # -1 and + 2 because we need to check for diagonally adjacent symbols, too
        for index in range(number_start_index - 1, number_stop_index + 2):
            # Can be out of bounds if a digit is the first/last element on the line
            if index < 0 or index > len(line) - 1:
                continue

            if is_symbol_at_index(line=line, index=index):
                return True

    return False


def is_number_adjacent_to_symbol(
    number_start_index: int,
    number_stop_index: int,
    current_line: str,
    previous_line: Optional[str],
    next_line: Optional[str],
) -> bool:
    """Checks if a symbol is adjacent to a number at given indices in any directions.

    Args:
        number_start_index: First index of the number on the current line
        number_stop_index: Last index of the number on the current line
        current_line: Line of the number being checked
        previous_line: Line before the current line
        next_line: Line after the current line

    Returns:
        True if there's an adjacent symbol in any of the directions, False otherwise
    """

    return is_horizontally_adjacent_symbol(
        number_start_index=number_start_index,
        number_stop_index=number_stop_index,
        current_line=current_line,
    ) or is_vertically_adjacent_symbol(
        number_start_index=number_start_index,
        number_stop_index=number_stop_index,
        previous_line=previous_line,
        next_line=next_line,
    )


def main() -> None:
    """Prints the sum of all the part numbers in the engine schematic."""

    lines: list[str] = read_file(filename="puzzle_input.txt")

    part_numbers_sum: int = 0
    digits: list[str] = []

    for line_index, line in enumerate(lines):
        current_line: str = line
        previous_line: Optional[str] = lines[line_index - 1] if line_index != 0 else None
        next_line: Optional[str] = lines[line_index + 1] if line_index != (len(lines) - 1) else None

        for character_index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
            if (character_index == len(line) - 1 or not line[character_index + 1].isdigit()) and digits:
                number_start_index: int = character_index - (len(digits) - 1)

                if is_number_adjacent_to_symbol(
                    number_start_index=number_start_index,
                    number_stop_index=character_index,
                    current_line=current_line,
                    previous_line=previous_line,
                    next_line=next_line,
                ):
                    part_numbers_sum += int("".join(digits))

                digits = []

    print(f"Part numbers sum: {part_numbers_sum}")


if __name__ == "__main__":
    main()
