from math import inf

from day_05.common import get_maps, ConversionMap, LowestLocationCalculator

FILE: str = "puzzle_input.txt"


def get_seed_ranges(line: str) -> list[range]:
    """Returns all seed ranges.

    Args:
        line: String of raw seed ranges data

    Returns:
        List of seed ranges
    """

    seed_ranges: list[int] = [int(number) for number in line.split(":")[1].split()]

    return [range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)]


def main() -> None:
    """Prints the solution to Day 5, Part Two."""

    lowest_location: int | float = inf
    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.read().split("\n\n")

    maps: list[list[ConversionMap]] = get_maps(lines=lines[1:])

    for seed_range in get_seed_ranges(line=lines[0]):
        location_calc: LowestLocationCalculator = LowestLocationCalculator(seed_range=seed_range)
        location: int = location_calc.get_location(maps=maps)

        if location < lowest_location:
            lowest_location = location

    print(lowest_location)


if __name__ == "__main__":
    main()
