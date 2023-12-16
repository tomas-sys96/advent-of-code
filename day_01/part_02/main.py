from day_01.helpers.common import read_file
from day_01.helpers.digits import DigitDataStorage

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all calibration values."""

    lines: list[str] = read_file(file_path=FILE_PATH)
    calibration_values_sum: int = 0

    for line in lines:
        # Create a dataclass to store the detected digits and their index on the line with
        digit_data_storage: DigitDataStorage = DigitDataStorage(digits_on_line={})
        digit_data_storage.update_digits_on_line(line=line)

        calibration_values_sum += digit_data_storage.get_calibration_value()
        del digit_data_storage

    print(calibration_values_sum)


if __name__ == "__main__":
    main()
