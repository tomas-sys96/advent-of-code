from typing import Optional

from day_03.common import read_file, Number, Symbol
from symbol_detector import SymbolDetector

FILE_PATH: str = "../test_input.txt"


def get_adjacent_lines(line_index: int, lines: list[str]) -> tuple[Optional[str], Optional[str]]:
    """"""

    previous_line: Optional[str] = lines[line_index - 1] if line_index != 0 else None
    next_line: Optional[str] = lines[line_index + 1] if line_index != (len(lines) - 1) else None

    return previous_line, next_line


def main() -> None:
    """Prints the sum of all the gear ratios in the engine schematic."""

    lines: list[str] = read_file(file_path=FILE_PATH)

    gear_ratios_sum: int = 0
    digits: list[str] = []

    for line_index, line in enumerate(lines):
        # There's no "previous"/"next" line for the first/last line
        previous_line: Optional[str]
        next_line: Optional[str]
        previous_line, next_line = get_adjacent_lines(line_index=line_index, lines=lines)

        for character_index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
            if (character_index == len(line) - 1 or not line[character_index + 1].isdigit()) and digits:
                number: Number = Number(
                    start_index=character_index - (len(digits) - 1),
                    stop_index=character_index,
                    line_index=line_index,
                    line=line,
                    previous_line=previous_line,
                    next_line=next_line,
                )
                detector: SymbolDetector = SymbolDetector(number=number)

                if detector.is_symbol_next_to_number():
                    detector.symbol.update_lines(
                        *get_adjacent_lines(
                            line_index=detector.symbol.line_index,
                            lines=lines,
                        )
                    )

                digits = []


if __name__ == "__main__":
    main()
