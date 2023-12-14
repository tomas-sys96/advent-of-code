from typing import Optional

from day_03.common import Number, Symbol

ASTERISK: str = "*"


class SymbolDetector:
    """Class for detecting symbols adjacent to a number at given indices.

    Attributes:
        number: Number at a given line and indices
    """

    _instance: Optional["SymbolDetector"] = None
    symbol: Symbol

    def __new__(cls, *args, **kwargs) -> "SymbolDetector":
        if not cls._instance:
            cls._instance = super(SymbolDetector, cls).__new__(cls)
        return cls._instance

    def __init__(self, number: Number) -> None:
        self.number: Number = number

    def _is_symbol_at_index(self, index: int, line_index: int, line: str) -> bool:
        """Checks if a character at a given index is a valid symbol.

        Args:
            index: Index of the character on the line
            line_index: Index of the line in the lines array
            line: Line containing the character to be checked as a symbol

        Returns:
            True if the character is a valid symbol (e.g. /, #, +, * etc.), False otherwise
        """

        # Get character at index
        if line[index] == ASTERISK:
            self.symbol = Symbol(
                index=index,
                line_index=line_index,
                line=line,
            )
            return True

        return False

    def _is_symbol_next_to_number_horizontally(self) -> bool:
        """Checks if there's a symbol adjacent to a number at given indices in the horizontal direction.

        Returns:
            True if there's an adjacent symbol, False otherwise
        """

        for index in (self.number.start_index - 1, self.number.stop_index + 1):
            # Can be out of bounds if a digit is the first/last element on the line
            if index < 0 or index > (len(self.number.line) - 1):
                continue

            if self._is_symbol_at_index(
                index=index,
                line_index=self.number.line_index,
                line=self.number.line,
            ):
                return True

        return False

    def _is_symbol_next_to_number_vertically(self) -> bool:
        """Checks if there's a symbol adjacent to a number at given indices in the vertical/diagonal direction.

        Returns:
            True if there's an adjacent symbol, False otherwise
        """

        for line in (self.number.previous_line, self.number.next_line):
            # A previous/next line may not exist -> skip to the next iteration
            if not line:
                continue
            # Get the current line's index so that we know where to find the symbol later
            line_index: int = (
                self.number.line_index - 1 if line is self.number.previous_line else self.number.line_index + 1
            )

            # -1 and + 2 because we need to check for diagonally adjacent symbols, too
            for index in range(self.number.start_index - 1, self.number.stop_index + 2):
                # Can be out of bounds if a digit is the first/last element on the line
                if index < 0 or index > len(line) - 1:
                    continue

                if self._is_symbol_at_index(
                    index=index,
                    line_index=line_index,
                    line=line,
                ):
                    return True

        return False

    def is_symbol_next_to_number(self) -> bool:
        """Checks if a symbol is adjacent to a number at given indices in any directions.

        Returns:
            True if there's an adjacent symbol in any of the directions, False otherwise
        """

        return self._is_symbol_next_to_number_horizontally() or self._is_symbol_next_to_number_vertically()
