from math import inf

from day_05.helpers import read_puzzle_input, get_maps, get_location, ConversionRange

FILE_PATH: str = "../puzzle_input.txt"


def get_seeds(line: str) -> list[int]:
    """Returns the seed numbers.

    Args:
        line: String with info about the ranges of seed numbers

    Returns:
        List of seed numbers
    """

    seed_ranges: list[int] = [int(number) for number in line.split(":")[1].split()]

    for number_index in range(0, len(seed_ranges), 2):
        range_start: int = seed_ranges[number_index]
        range_length = seed_ranges[number_index + 1]
        for seed in range(range_start, range_start + range_length):
            yield seed


def main() -> None:
    """Prints the solution to Day 5, Part Two."""

    lowest_location: float = inf
    lines: list[str] = read_puzzle_input(file_path=FILE_PATH)

    maps: list[list[ConversionRange]] = get_maps(lines=lines[1:])

    for seed in get_seeds(line=lines[0]):
        location: int = get_location(seed=seed, maps=maps)

        if location < lowest_location:
            lowest_location = location

    print(lowest_location)


if __name__ == "__main__":
    main()
