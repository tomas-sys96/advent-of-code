from day_01.digits import get_digits_on_line, get_calibration_value

FILE: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 1, Part Two."""

    total: int = 0
    with open(file=FILE, mode="r") as file:
        lines: list[str] = [line.replace("\n", "") for line in file.readlines()]

    for line in lines:
        # Create a dictionary with digits and their indices on the line
        # Obtain the first and the last digit, add them together and update the sum of calibration values
        total += get_calibration_value(digits_on_line=get_digits_on_line(line=line))

    print(total)


if __name__ == "__main__":
    main()
