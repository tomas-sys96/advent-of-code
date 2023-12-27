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
