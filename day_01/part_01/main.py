from day_01.helpers.common import read_file

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all the calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    first_digit: str = ""
    last_digit: str = ""
    calibration_values_sum: int = 0

    for line in lines:
        for character in line:
            if character.isdigit():
                first_digit = character
                break
        for character in reversed(line):
            if character.isdigit():
                last_digit = character
                break

        if first_digit and last_digit:
            calibration_values_sum += int("".join([first_digit, last_digit]))

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
