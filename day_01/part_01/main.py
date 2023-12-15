FILE_PATH: str = "../puzzle_input.txt"


def read_file(file_path: str) -> list[str]:
    """Reads a text file and returns its contents as a list of strings.

    Args:
        file_path: Path to the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=file_path, mode="r") as file:
        return [line.replace("\n", "") for line in file.readlines()]


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
