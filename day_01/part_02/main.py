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


def main() -> None:
    """Prints the sum of all calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    calibration_values_sum: int = 0

    for line in lines:
        # Create a dictionary to store the detected digits and their index on the line in
        digits_on_line: dict[int, str] = {}
        for character_index, character in enumerate(line):
            if character.isdigit():
                # Store the detected digits right away
                digits_on_line[character_index] = character
            else:
                # Check if a substring equals to a digit as a word
                for digit_as_word, digit in digits.items():
                    if line[character_index : (character_index + len(digit_as_word))] == digit_as_word:
                        digits_on_line[character_index] = digit
                        break

        # Find the first and the last digit
        first_digit: str = digits_on_line[min(digits_on_line.keys())]
        last_digit: str = digits_on_line[max(digits_on_line.keys())]

        calibration_values_sum += int(first_digit + last_digit)

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
