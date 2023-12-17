from common import read_file, FILE_PATH
from day_01.digits import get_digits_on_line, get_calibration_value


def main() -> None:
    """Prints the solution to Day 1, Part Two."""

    total: int = 0
    lines: list[str] = read_file(file_path=FILE_PATH)

    for line in lines:
        # Create a dictionary with digits and their indices on the line
        # Obtain the first and the last digit, add them together and update the sum of calibration values
        total += get_calibration_value(digits_on_line=get_digits_on_line(line=line))

    print(total)


if __name__ == "__main__":
    main()
