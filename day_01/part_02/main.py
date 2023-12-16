from day_01.helpers.common import read_file

FILE_PATH: str = "../test_input.txt"

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


def get_letters_to_skip() -> str:
    """Returns a string of letters that are not present in any of the digits word representations.

    Returns:
        String of unused letters
    """

    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    unused_letters: str = ""
    for letter in alphabet:
        matches: bool = False
        for digit_as_word in digits.keys():
            if letter in digit_as_word:
                matches = True
                break
        if not matches:
            unused_letters += letter

    return unused_letters


def main() -> None:
    """Prints the sum of all the calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    letters_to_skip: str = get_letters_to_skip()
    calibration_values_sum: int = 0

    for line in lines:
        word: str = ""
        digits_on_line: list[str] = []

        for character in line:
            if character.isdigit():
                digits_on_line.append(character)
            else:
                if character in letters_to_skip:
                    continue

                for digit_as_word in digits.keys():
                    if digit_as_word.startswith(word + character):
                        word += character
                        break
                    elif digit_as_word.startswith(character) and word:
                        word = character
                        continue

                if word in digits.keys():
                    digits_on_line.append(digits[word])
                    word = ""

        try:
            calibration_values_sum += int("".join([digits_on_line[0], digits_on_line[-1]]))
        except IndexError:
            pass

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
