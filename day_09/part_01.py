from common import get_sequences

FILE: str = "puzzle_input.txt"


def get_extrapolated_value(sequences: list[list[int]]) -> int:
    """Returns the extrapolated value for the initial sequence.

    Args:
        sequences: List of sequences

    Returns:
        Extrapolated value
    """

    extrapolated_value: int = 0
    for i in reversed(range(0, len(sequences) - 1)):
        extrapolated_value += sequences[i][-1]

    return extrapolated_value


def main() -> None:
    """Prints the solution to Day 9, Part One."""

    total_sum: int = 0
    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.readlines()

    for line in lines:
        sequences: list[list[int]] = get_sequences(line=line)
        total_sum += get_extrapolated_value(sequences=sequences)

    print(total_sum)


if __name__ == "__main__":
    main()
