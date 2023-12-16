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


def get_digits_on_line(line: str) -> dict[int, str]:
    """Returns a dictionary with digits and their indices for a given line.

    Args:
        line: Line to be checked

    Returns:
        digits_on_line: Dictionary with digits and their indices
    """

    digits_on_line: dict[int, str] = {}

    for character_index, character in enumerate(line):
        if character.isdigit():
            # Store the detected digits right away
            digits_on_line[character_index] = character
        else:
            # Check if a substring starting at the current index equals to a digit as a word
            for digit_as_word, digit in digits.items():
                if line[character_index : (character_index + len(digit_as_word))] == digit_as_word:
                    digits_on_line[character_index] = digit
                    break

    return digits_on_line


def get_calibration_value(digits_on_line: dict[int, str]) -> int:
    """Returns the calibration value for the current line.

    Args:
        digits_on_line: Dictionary with digits and their indices

    Returns:
        Calibration value
    """

    first_digit: str = digits_on_line[min(digits_on_line.keys())]
    last_digit: str = digits_on_line[max(digits_on_line.keys())]

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
