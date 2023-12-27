from collections import namedtuple

FILE_PATH: str = "../puzzle_input.txt"
Sequence: namedtuple = namedtuple(typename="Sequence", field_names=["first_value", "last_value"])


def get_sequences(line: str) -> list[list[int]]:
    """Returns sequences of numbers, based on the initial sequence.

    Args:
        line: String with numbers

    Returns:
        List of sequences
    """

    sequences: list[list[int]] = [[int(number) for number in line.removesuffix("\n").split()]]

    while not sequences[-1][0] == sequences[-1][-1] == 0:
        sequences.append([sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)])

    return sequences


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
    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    for line in lines:
        sequences: list[list[int]] = [[int(number) for number in line.removesuffix("\n").split()]]

        while not sequences[-1][0] == sequences[-1][-1] == 0:
            sequences.append([sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)])

        total_sum += get_extrapolated_value(sequences=sequences)

    print(total_sum)


if __name__ == "__main__":
    main()
