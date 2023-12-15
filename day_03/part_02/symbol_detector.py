from typing import Optional

from day_03.common import Number, Symbol

ASTERISK: str = "*"


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
    def _is_symbol(character: str) -> bool:
        """Checks if a character is a valid symbol.

        Args:
            character: Character to be validated as an asterisk symbol

        Returns:
            True if the character is a valid symbol (e.g. /, #, +, * etc.), False otherwise
        """

        return character == ASTERISK

    def _find_symbol_next_to_number_horizontally(self) -> Optional[Symbol]:
        """Checks for an asterisk symbol adjacent to the current number in the horizontal direction.

        Returns:
            Symbol object if there is an asterisk symbol next to the number, None otherwise
        """

        for index in (self.number.start_index - 1, self.number.stop_index + 1):
            # Can be out of bounds if a digit is the first/last element on the line
            if index < 0 or index > (len(self.number.line) - 1):
                continue

            if self._is_symbol(character=self.number.line[index]):
                return Symbol(index=index, line_index=self.number.line_index)

    def _find_symbol_next_to_number_vertically(self) -> Optional[Symbol]:
        """Checks for an asterisk symbol adjacent to the current number in the vertical/diagonal direction.

        Returns:
            Symbol object if there is an asterisk symbol next to the number, None otherwise
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

                if self._is_symbol(character=line[index]):
                    return Symbol(index=index, line_index=line_index)

    def find_symbol_next_to_number(self) -> Optional[Symbol]:
        """Checks for an asterisk symbol adjacent to the current number.

        Returns:
            Symbol object if there is an asterisk symbol next to the number, None otherwise
        """

        return self._find_symbol_next_to_number_horizontally() or self._find_symbol_next_to_number_vertically()
