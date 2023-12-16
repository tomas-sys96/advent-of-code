from common import read_file
from day_01.digits import get_first_digit

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    calibration_values_sum: int = 0

    for line in lines:
        # For the first digit, iterate over the line in the forward direction
        first_digit: str = get_first_digit(array=line)
        # For the last digit, iterate over the line in the backward direction
        last_digit: str = get_first_digit(array=reversed(line))

        calibration_values_sum += int(first_digit + last_digit)

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
