from typing import Optional, Type
from collections import namedtuple

from day_03.common import read_file, Number
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

    SymbolData: Type[tuple] = namedtuple(typename="SymbolData", field_names=["index", "adjacent_numbers"])
    detected_symbols: dict = {}

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
                    value=int("".join([*digits])),
                    start_index=character_index - (len(digits) - 1),
                    stop_index=character_index,
                    line_index=line_index,
                    line=line,
                    previous_line=previous_line,
                    next_line=next_line,
                )
                detector: SymbolDetector = SymbolDetector(number=number)

                if detector.is_symbol_next_to_number():
                    # detected_symbols = {
                    #     line_index_0: [
                    #         SymbolData(index=index_0, adjacent_numbers=[936, 672]),
                    #         SymbolData(index=index_1, adjacent_numbers=[4, 24]),
                    #     ],
                    #     line_index_1: [
                    #         SymbolData(index=index_0, adjacent_numbers=[390, 425]),
                    #     ],
                    # }

                    symbol_found: bool = False

                    try:
                        # Attempt to append a new number to SymbolData.adjacent_numbers if the index
                        # matches with an existing symbol
                        for symbol_data_index, symbol_data in enumerate(detected_symbols[detector.symbol.line_index]):
                            if symbol_data.index == detector.symbol.index:
                                detected_symbols[detector.symbol.line_index][symbol_data_index].adjacent_numbers.append(
                                    number.value
                                )
                                symbol_found = True
                                break
                    except KeyError:
                        pass

                    if not symbol_found:
                        try:
                            # If it's a new symbol, attempt to append a new SymbolData element
                            detected_symbols[detector.symbol.line_index].append(
                                SymbolData(
                                    index=detector.symbol.index,
                                    adjacent_numbers=[number.value],
                                ),
                            )
                        except KeyError:
                            # If there isn't such line index key, add it in
                            detected_symbols[detector.symbol.line_index] = [
                                SymbolData(
                                    index=detector.symbol.index,
                                    adjacent_numbers=[number.value],
                                ),
                            ]

                digits = []


if __name__ == "__main__":
    main()
