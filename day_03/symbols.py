from collections import namedtuple
from dataclasses import dataclass
from math import prod
from typing import Optional, Callable, Type

from day_03.helpers import Number

PERIOD: str = "."
ASTERISK: str = "*"

SymbolDataPoint: Type[tuple] = namedtuple(typename="SymbolDataPoint", field_names=["index", "adjacent_numbers"])


@dataclass
class Symbol:
    index: int
    line_index: int


@dataclass
class SymbolDataStorage:
    detected_symbols: dict

    def add_symbol_data(self, symbol: Symbol, number: Number) -> None:
        """Adds a symbol data point to the dictionary of detected symbols.

        Args:
            symbol: Symbol object
            number: Number object
        """

        # detected_symbols = {
        #     line_index_0: [
        #         SymbolDataPoint(index=index_0, adjacent_numbers=[number_1, number_2]),
        #         SymbolDataPoint(index=index_1, adjacent_numbers=[number_3, number_4]),
        #     ],
        #     line_index_1: [
        #         SymbolDataPoint(index=index_0, adjacent_numbers=[number_5, number_6]),
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
                    SymbolDataPoint(
                        index=symbol.index,
                        adjacent_numbers=[number.value],
                    ),
                )
            except KeyError:
                # If there isn't such line index key, add it in
                self.detected_symbols[symbol.line_index] = [
                    SymbolDataPoint(
                        index=symbol.index,
                        adjacent_numbers=[number.value],
                    ),
                ]

    def get_gear_ratios_sum(self) -> int:
        """Calculates and returns the sum of all gear ratios, i.e. where the asterisk symbol is adjacent to exactly
        two part numbers.

        Returns:
            gear_ratios_sum: Sum of all gear ratios
        """

        gear_ratios_sum: int = 0

        for symbols in self.detected_symbols.values():
            for symbol in symbols:
                if len(symbol.adjacent_numbers) == 2:
                    gear_ratios_sum += prod(symbol.adjacent_numbers)

        return gear_ratios_sum


class SymbolDetector:
    """Class for detecting symbols adjacent to a number at given indices.

    Attributes:
        number: Number at a given line and indices
    """

    _instance: Optional["SymbolDetector"] = None

    def __new__(cls, *args, **kwargs) -> "SymbolDetector":
        if not cls._instance:
            cls._instance = super(SymbolDetector, cls).__new__(cls)
        return cls._instance

    def __init__(self, number: Number) -> None:
        self.number: Number = number

    @staticmethod
    def _is_any_symbol(character: str) -> bool:
        """Checks if a character is a symbol.

        Args:
            character: Character to be validated as a symbol

        Returns:
            True if the character is a valid symbol (e.g. /, #, +, * etc.), False otherwise
        """

        return not character.isdigit() and not character == PERIOD

    @staticmethod
    def _is_asterisk_symbol(character: str) -> bool:
        """Checks if a character is an asterisk symbol.

        Args:
            character: Character to be validated as an asterisk symbol

        Returns:
            True if the character is an asterisk symbol, False otherwise
        """

        return character == ASTERISK

    def _find_symbol_next_to_number_horizontally(self, is_symbol: Callable) -> Optional[Symbol]:
        """Checks for a symbol adjacent to the current number in the horizontal direction.

        Args:
            is_symbol: Function that validates characters as the target symbol

        Returns:
            Symbol object if there is a symbol next to the number, None otherwise
        """

        for index in (self.number.start_index - 1, self.number.stop_index + 1):
            # Can be out of bounds if a digit is the first/last element on the line
            if index < 0 or index > (len(self.number.line) - 1):
                continue

            if is_symbol(character=self.number.line[index]):
                return Symbol(index=index, line_index=self.number.line_index)

    def _find_symbol_next_to_number_vertically(self, is_symbol: Callable) -> Optional[Symbol]:
        """Checks for a symbol adjacent to the current number in the vertical/diagonal direction.

        Args:
            is_symbol: Function that validates characters as the target symbol

        Returns:
            Symbol object if there is a symbol next to the number, None otherwise
        """

        for line in (self.number.previous_line, self.number.next_line):
            # A previous/next line may not exist -> skip to the next iteration
            if not line:
                continue
            # Get the current line's index so that we know on which line to find the symbol
            line_index: int = (
                self.number.line_index - 1 if line is self.number.previous_line else self.number.line_index + 1
            )

            # -1 and + 2 because we need to check for diagonally adjacent symbols, too
            for index in range(self.number.start_index - 1, self.number.stop_index + 2):
                # Can be out of bounds if a digit is the first/last element on the line
                if index < 0 or index > len(line) - 1:
                    continue

                if is_symbol(character=line[index]):
                    return Symbol(index=index, line_index=line_index)

    def find_symbol_next_to_number(self, symbol: Optional[str] = None) -> Optional[Symbol]:
        """Checks for a symbol adjacent to the current number.

        Args:
            symbol: Symbol to look for

        Returns:
            Symbol object if there is a symbol next to the number, None otherwise
        """

        validation_function: Callable = self._is_asterisk_symbol if symbol == "*" else self._is_any_symbol

        return self._find_symbol_next_to_number_horizontally(
            is_symbol=validation_function,
        ) or self._find_symbol_next_to_number_vertically(
            is_symbol=validation_function,
        )
