from typing import Optional

from common import get_adjacent_lines, Number, SymbolDataStorage, SymbolDetector, Symbol

FILE: str = "puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 3, Part Two."""

    with open(file=FILE, mode="r") as file:
        lines: list[str] = [line.replace("\n", "") for line in file.readlines()]

    digits: list[str] = []
    symbol_data_storage: SymbolDataStorage = SymbolDataStorage(detected_symbols={})

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

                symbol: Optional[Symbol] = detector.find_symbol_next_to_number(symbol="*")
                if symbol:
                    symbol_data_storage.add_symbol_data(symbol=symbol, number=number)

                digits = []
                # Delete the number and symbol objects from memory
                del number, symbol

    print(symbol_data_storage.get_gear_ratios_sum())


if __name__ == "__main__":
    main()
