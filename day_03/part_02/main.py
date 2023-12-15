from typing import Optional

from day_03.common import read_file, Number, Symbol, SymbolDataStorage, get_adjacent_lines
from symbol_detector import SymbolDetector

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all the gear ratios in the engine schematic."""

    lines: list[str] = read_file(file_path=FILE_PATH)
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

                symbol: Optional[Symbol] = detector.find_symbol_next_to_number()
                if symbol:
                    symbol_data_storage.add_symbol_data(symbol=symbol, number=number)

                digits = []
                # Delete the number object from memory
                del number

    # print(symbol_data_storage.get_gear_ratios_sum())


if __name__ == "__main__":
    # main()

    import timeit
    print(f"Time taken: {timeit.timeit(main, number=1000)} seconds")
