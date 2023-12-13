from typing import Optional

PERIOD: str = "."


class SymbolDetector:
    """Class for detecting symbols adjacent to a number at given indices.

    Attributes:
        number_start_index: First index of the number on the current line
        number_stop_index: Last index of the number on the current line
        current_line: Line of the number being checked
        previous_line: Line before the current line
        next_line: Line after the current line
    """

    _instance: Optional["SymbolDetector"] = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SymbolDetector, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        number_start_index: int,
        number_stop_index: int,
        current_line: str,
        previous_line: Optional[str],
        next_line: Optional[str],
    ) -> None:
        self.number_start_index: int = number_start_index
        self.number_stop_index: int = number_stop_index
        self.current_line: str = current_line
        self.previous_line: Optional[str] = previous_line
        self.next_line: Optional[str] = next_line

    @staticmethod
    def _is_symbol_at_index(line: str, index: int) -> bool:
        """Checks if a character at a given index is a valid symbol.

        Args:
            line: Line containing the character to be checked as a symbol
            index: Index of the character on the line

        Returns:
            True if the character is a valid symbol (e.g. /, #, +, * etc.), False otherwise
        """

        character: str = line[index]
        return not character.isdigit() and not character == PERIOD

    def _is_symbol_next_to_number_horizontally(self) -> bool:
        """Checks if there's a symbol adjacent to a number at given indices in the horizontal direction.

        Returns:
            True if there's an adjacent symbol, False otherwise
        """

        for index in (self.number_start_index - 1, self.number_stop_index + 1):
            # Can be out of bounds if a digit is the first/last element on the line
            if index < 0 or index > (len(self.current_line) - 1):
                continue

            if self._is_symbol_at_index(line=self.current_line, index=index):
                return True

        return False

    def _is_symbol_next_to_number_vertically(self) -> bool:
        """Checks if there's a symbol adjacent to a number at given indices in the vertical/diagonal direction.

        Returns:
            True if there's an adjacent symbol, False otherwise
        """

        for line in (self.previous_line, self.next_line):
            # A previous/next line may not exist -> skip to the next iteration
            if not line:
                continue
            # -1 and + 2 because we need to check for diagonally adjacent symbols, too
            for index in range(self.number_start_index - 1, self.number_stop_index + 2):
                # Can be out of bounds if a digit is the first/last element on the line
                if index < 0 or index > len(line) - 1:
                    continue

                if self._is_symbol_at_index(line=line, index=index):
                    return True

        return False

    def is_symbol_next_to_number(self) -> bool:
        """Checks if a symbol is adjacent to a number at given indices in any directions.

        Returns:
            True if there's an adjacent symbol in any of the directions, False otherwise
        """

        return self._is_symbol_next_to_number_horizontally() or self._is_symbol_next_to_number_vertically()
