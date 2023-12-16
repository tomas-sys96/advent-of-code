from dataclasses import dataclass

digits: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


@dataclass
class DigitDataStorage:
    digits_on_line: dict[int, str]

    def update_digits_on_line(self, line: str) -> None:
        """Adds digits and their indices for a given line to a dictionary.

        Args:
            line: Line to be checked
        """

        for character_index, character in enumerate(line):
            if character.isdigit():
                # Store the detected digits right away
                self.digits_on_line[character_index] = character
            else:
                # Check if a substring starting at the current index equals to a digit as a word
                for digit_as_word, digit in digits.items():
                    if line[character_index : (character_index + len(digit_as_word))] == digit_as_word:
                        self.digits_on_line[character_index] = digit
                        break

    def get_calibration_value(self) -> int:
        """Returns the calibration value for the current line.

        Returns:
            Calibration value
        """

        first_digit: str = self.digits_on_line[min(self.digits_on_line.keys())]
        last_digit: str = self.digits_on_line[max(self.digits_on_line.keys())]

        return int(first_digit + last_digit)


def get_first_digit(array: str | reversed) -> str:
    """Returns the first digit in an array.

    Args:
        array: Iterable string object

    Returns:
        Digit as a string
    """

    for character in array:
        if character.isdigit():
            return character
