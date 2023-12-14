from typing import Optional
from symbol_detector import SymbolDetector


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

                symbol_detector: SymbolDetector = SymbolDetector(
                    number_start_index=number_start_index,
                    number_stop_index=character_index,
                    current_line=current_line,
                    previous_line=previous_line,
                    next_line=next_line,
                )

                if symbol_detector.is_symbol_next_to_number():
                    part_numbers_sum += int("".join(digits))

                digits = []

    print(part_numbers_sum)


if __name__ == "__main__":
    main()
