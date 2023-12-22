from math import inf

from day_05.helpers import read_puzzle_input, get_maps, ConversionMap

FILE_PATH: str = "../test_input.txt"


def get_seed_ranges(line: str) -> list[range]:
    """Returns all seed ranges.

    Args:
        line: String of raw seed ranges data

    Returns:
        List of seed ranges
    """

    seed_ranges: list[int] = [int(number) for number in line.split(":")[1].split()]

    return [range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)]


def get_location_for_seed_range(seed_range: range, maps: list[list[ConversionMap]]) -> int:
    """"""

    # TODO: Create the Range dataclass, and make destination_ranges a set of these ranges
    # class Range:
    #     def __init__(self, start, end):
    #         self.start = start
    #         self.end = end
    #
    #     def get_range_object(self):
    #         return range(self.start, self.end)

    source_ranges: list[range]
    destination_ranges: list[range] = [seed_range]

    for mapping in maps:
        source_ranges = destination_ranges.copy()
        destination_ranges.clear()
        for source_range in source_ranges:
            for conversion_map in mapping:
                source_range_start: int = source_range.start
                range_length: int = source_range.stop - source_range.start
                conversion_map_range: range = range(
                    conversion_map.source_range_start,
                    conversion_map.source_range_start + conversion_map.range_length,
                )

                # Check if there's a full/partial overlap of ranges
                if any(source in conversion_map_range for source in [source_range.start, source_range.stop - 1]):
                    # Check if the first source falls into the conversion map range
                    # If it doesn't, separate a new range from the original source range
                    if source_range.start not in conversion_map_range:
                        destination_ranges.append(
                            range(
                                source_range.start,
                                conversion_map_range.start,
                            )
                        )
                        # Set new range start and length accordingly
                        source_range_start = conversion_map_range.start
                        range_length = source_range.stop - source_range_start

                    # Check if the last source falls into the conversion map range
                    # If it doesn't, separate a new range from the original source range
                    if source_range.stop - 1 not in conversion_map_range:
                        destination_ranges.append(
                            range(
                                conversion_map_range.stop,
                                source_range.stop,
                            )
                        )
                        range_length = conversion_map_range.stop - source_range.start

                    shift: int = conversion_map.destination_range_start - conversion_map.source_range_start

                    # Add the overlapping subset of the original source range to the list of destination ranges
                    destination_ranges.append(
                        range(
                            source_range_start + shift,
                            source_range_start + shift + range_length,
                        )
                    )

            if not destination_ranges:
                # Add the whole unchanged source range to the list of destination ranges
                # if there are no overlaps at all
                destination_ranges.append(
                    range(
                        source_range.start,
                        source_range.stop,
                    )
                )


def main() -> None:
    """Prints the solution to Day 5, Part Two."""

    lowest_location: float = inf
    lines: list[str] = read_puzzle_input(file_path=FILE_PATH)

    maps: list[list[ConversionMap]] = get_maps(lines=lines[1:])

    for seed_range in get_seed_ranges(line=lines[0]):
        location: int = get_location_for_seed_range(seed_range=seed_range, maps=maps)

        if location < lowest_location:
            lowest_location = location

    print(lowest_location)


if __name__ == "__main__":
    main()
