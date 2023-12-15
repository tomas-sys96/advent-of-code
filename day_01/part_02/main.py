from day_01.helpers.common import read_file

FILE_PATH: str = "../puzzle_input.txt"

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


def get_characters_to_skip() -> str:
    """"""

    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    unused_characters: str = ""
    for character in alphabet:
        matches: bool = False
        for digit_as_letter in digits.keys():
            if character in digit_as_letter:
                matches = True
                break
        if not matches:
            unused_characters += character

    return unused_characters


def main() -> None:
    """Prints the sum of all the calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    characters_to_skip: str = get_characters_to_skip()
    calibration_values_sum: int = 0

    for line in lines:
        current_digit: str = ""
        digits_on_line: list[str] = []

        for character in line:
            if character.isdigit():
                digits_on_line.append(character)
            else:
                if character in characters_to_skip:
                    continue
                for digit_as_letter in digits.keys():
                    if digit_as_letter.startswith(current_digit + character):
                        current_digit += character
                        break
                if current_digit in digits.keys():
                    digits_on_line.append(digits[current_digit])
                    current_digit = ""

        if len(digits_on_line) >= 2:
            calibration_values_sum += int("".join([digits_on_line[0], digits_on_line[-1]]))

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
