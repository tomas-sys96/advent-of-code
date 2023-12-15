from collections import namedtuple
from dataclasses import dataclass
from typing import Optional, Type
from math import prod

SymbolData: Type[tuple] = namedtuple(typename="SymbolData", field_names=["index", "adjacent_numbers"])


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


@dataclass
class SymbolDataStorage:
    detected_symbols: dict

    def add_symbol_data(self, symbol: Symbol, number: Number) -> None:
        """"""

        # detected_symbols = {
        #     line_index_0: [
        #         SymbolData(index=index_0, adjacent_numbers=[number_1, number_2]),
        #         SymbolData(index=index_1, adjacent_numbers=[number_3, number_4]),
        #     ],
        #     line_index_1: [
        #         SymbolData(index=index_0, adjacent_numbers=[number_5, number_6]),
        #     ],
        # }

        symbol_found: bool = False

        try:
            # Attempt to append a new number to SymbolData.adjacent_numbers if the index
            # matches with an existing symbol
            for symbol_data_index, symbol_data in enumerate(self.detected_symbols[symbol.line_index]):
                if symbol_data.index == symbol.index:
                    self.detected_symbols[symbol.line_index][symbol_data_index].adjacent_numbers.append(number.value)
                    symbol_found = True
                    break
        except KeyError:
            pass

        if not symbol_found:
            try:
                # If it's a new symbol, attempt to append a new SymbolData element
                self.detected_symbols[symbol.line_index].append(
                    SymbolData(
                        index=symbol.index,
                        adjacent_numbers=[number.value],
                    ),
                )
            except KeyError:
                # If there isn't such line index key, add it in
                self.detected_symbols[symbol.line_index] = [
                    SymbolData(
                        index=symbol.index,
                        adjacent_numbers=[number.value],
                    ),
                ]

    def get_gear_ratios_sum(self) -> int:
        """"""

        gear_ratios_sum: int = 0

        for symbols in self.detected_symbols.values():
            for symbol in symbols:
                if len(symbol.adjacent_numbers) == 2:
                    gear_ratios_sum += prod(symbol.adjacent_numbers)

        return gear_ratios_sum


def read_file(file_path: str) -> list[str]:
    """Reads a text file and returns its contents as a list of strings.

    Args:
        file_path: Path to the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=file_path, mode="r") as file:
        return [line.replace("\n", "") for line in file.readlines()]
