from math import inf

from day_05.helpers import read_puzzle_input, get_maps, ConversionMap

FILE_PATH: str = "../puzzle_input.txt"


def get_location(seed: int, maps: list[list[ConversionMap]]) -> int:
    """Converts a seed number to a location number.

    Args:
        seed: Seed number
        maps: List of conversion map lists

    Returns:
        destination: Location number (i.e. the final destination number)
    """

    destination: int = seed

    for mapping in maps:
        for conversion_map in mapping:
            if destination in range(
                conversion_map.source_range_start, conversion_map.source_range_start + conversion_map.range_length
            ):
                destination = conversion_map.destination_range_start + (destination - conversion_map.source_range_start)
                break

    return destination


def main() -> None:
    """Prints the solution to Day 5, Part One."""

    lowest_location: float = inf
    lines: list[str] = read_puzzle_input(file_path=FILE_PATH)

    maps: list[list[ConversionMap]] = get_maps(lines=lines[1:])
    seeds: list[int] = [int(number) for number in lines[0].split(":")[1].split()]

    for seed in seeds:
        location: int = get_location(seed=seed, maps=maps)

        if location < lowest_location:
            lowest_location = location

    print(lowest_location)


if __name__ == "__main__":
    main()
