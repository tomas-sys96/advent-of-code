from common import read_puzzle_input
from day_01.digits import get_first_digit


def main() -> None:
    """Prints the solution to Day 1, Part One."""

    total: int = 0
    lines: list[str] = read_puzzle_input()

    for line in lines:
        # For the first digit, iterate over the line in the forward direction
        first_digit: str = get_first_digit(array=line)
        # For the last digit, iterate over the line in the backward direction
        last_digit: str = get_first_digit(array=reversed(line))

        total += int(first_digit + last_digit)

    print(total)


if __name__ == "__main__":
    main()
