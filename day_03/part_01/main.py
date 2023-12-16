from typing import Optional

from common import read_file
from day_03.helpers import get_adjacent_lines, Number
from day_03.symbols import SymbolDetector, Symbol

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all the part numbers in the engine schematic."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    digits: list[str] = []
    part_numbers_sum: int = 0

    for line_index, line in enumerate(lines):
        previous_line: Optional[str]
        next_line: Optional[str]
        previous_line, next_line = get_adjacent_lines(line_index=line_index, lines=lines)

        for character_index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
            if (character_index == len(line) - 1 or not line[character_index + 1].isdigit()) and digits:
                number: Number = Number(
                    value=int("".join([*digits])),
                    start_index=character_index - (len(digits) - 1),
                    stop_index=character_index,
                    line_index=line_index,
                    line=line,
                    previous_line=previous_line,
                    next_line=next_line,
                )
                detector: SymbolDetector = SymbolDetector(number=number)

                symbol: Optional[Symbol] = detector.find_symbol_next_to_number()
                if symbol:
                    part_numbers_sum += int("".join(digits))

                digits = []
                # Delete the number and symbol objects from memory
                del number, symbol

    print(part_numbers_sum)


if __name__ == "__main__":
    main()
