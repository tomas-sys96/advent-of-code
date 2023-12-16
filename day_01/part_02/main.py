from common import read_file
from day_01.digits import get_digits_on_line, get_calibration_value

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    calibration_values_sum: int = 0

    for line in lines:
        # Create a dictionary with digits and their indices on the line
        # Obtain the first and the last digit, add them together and update the sum of calibration values
        calibration_values_sum += get_calibration_value(digits_on_line=get_digits_on_line(line=line))

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
