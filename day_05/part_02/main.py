from math import inf

from day_05.helpers import read_puzzle_input, get_maps, ConversionMap

FILE_PATH: str = "../puzzle_input.txt"


def get_seed_ranges(line: str) -> list[range]:
    """Returns all seed ranges.

    Args:
        line: String of raw seed ranges data

    Returns:
        List of seed ranges
    """

    seed_ranges: list[int] = [int(number) for number in line.split(":")[1].split()]

    return [range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)]


def get_sorted_ranges(ranges: list[range]) -> list[range]:
    """Sorts ranges by their start in ascending order.

    Args:
        ranges: List of ranges

    Returns:
        Sorted ranges
    """

    return sorted(ranges, key=lambda r: r.start)


def get_unchanged_source_ranges(source_range: range, overlapping_ranges: list[range]) -> list[range]:
    """Returns a list of source ranges that had no overlap with any conversion map ranges.

    Args:
        source_range: Original source range
        overlapping_ranges: Subsets of the original source range with overlap

    Returns:
        Subsets of the original source range with no overlap
    """

    sorted_ranges: list[range] = get_sorted_ranges(ranges=overlapping_ranges)

    # First range
    unchanged_ranges: list[range] = [range(source_range.start, sorted_ranges[0].start)]
    # Ranges in between
    for i in range(0, len(sorted_ranges) - 1):
        range_start: int = sorted_ranges[i].stop
        range_length: int = sorted_ranges[i + 1].start - sorted_ranges[i].stop
        unchanged_ranges.append(range(range_start, range_start + range_length))
    # Last range
    unchanged_ranges.append(range(sorted_ranges[-1].stop, source_range.stop))

    # Remove empty ranges from the list
    return [r for r in unchanged_ranges if r]


def ranges_overlap(source_range: range, conversion_map_range: range) -> bool:
    """Checks if the source and conversion map ranges have elements in common.

    Args:
        source_range: Source range
        conversion_map_range: Conversion map range

    Returns:
        True if either of the ranges overlaps the other, False otherwise
    """

    if any(source in conversion_map_range for source in [source_range.start, source_range.stop - 1]):
        return True

    if any(source in source_range for source in [conversion_map_range.start, conversion_map_range.stop - 1]):
        return True

    return False


def get_range_parameters(source_range: range, conversion_map_range: range) -> tuple[int, int]:
    """Returns range parameters based on the overlap between the source and conversion map ranges.

    Args:
        source_range: Source range
        conversion_map_range: Conversion map range

    Returns:
        tuple:
            source_range_start: Source range start,
            range_length: Range length
    """

    source_range_start: int = source_range.start
    range_length: int = source_range.stop - source_range.start

    # Check if the first source falls into the conversion map range
    if source_range.start not in conversion_map_range:
        source_range_start = conversion_map_range.start
        range_length = source_range.stop - source_range_start

    # Check if the last source falls into the conversion map range
    if source_range.stop - 1 not in conversion_map_range:
        range_length = conversion_map_range.stop - source_range_start

    return source_range_start, range_length


def get_min_location_for_seed_range(seed_range: range, maps: list[list[ConversionMap]]) -> int:
    """Returns the lowest location number for a range of seed numbers.

    Args:
        seed_range: Range of seed numbers
        maps: List of conversion mappings

    Returns:
        Location number
    """

    source_ranges: list[range]
    destination_ranges: list[range] = [seed_range]
    overlapping_ranges: list[range] = []

    for mapping in maps:
        source_ranges = destination_ranges.copy()
        destination_ranges.clear()
        for source_range in source_ranges:
            overlapping_ranges.clear()
            for conversion_map in mapping:
                conversion_map_range: range = range(
                    conversion_map.source_range_start,
                    conversion_map.source_range_start + conversion_map.range_length,
                )

                # Check if there's a full/partial overlap of ranges
                if ranges_overlap(source_range=source_range, conversion_map_range=conversion_map_range):
                    source_range_start, range_length = get_range_parameters(
                        source_range=source_range,
                        conversion_map_range=conversion_map_range,
                    )

                    shift: int = conversion_map.destination_range_start - conversion_map.source_range_start

                    # Add the overlapping part of the source range to overlapping ranges
                    overlapping_ranges.append(
                        range(
                            source_range_start,
                            source_range_start + range_length,
                        )
                    )
                    # Add the shifted overlapping part of the source range to destination ranges
                    destination_ranges.append(
                        range(
                            source_range_start + shift,
                            source_range_start + shift + range_length,
                        )
                    )

            if not overlapping_ranges:
                # Add the whole unchanged source range to destination ranges if there are no overlaps at all
                destination_ranges.append(
                    range(
                        source_range.start,
                        source_range.stop,
                    )
                )
            else:
                # Find the unchanged ranges and add them to destination ranges
                # Ignore the scenario of full overlap between the source range and one of the conversion map ranges
                # (meaning that there are no unchanged ranges)
                if not (len(overlapping_ranges) == 1 and overlapping_ranges[0] == source_range):
                    destination_ranges.extend(
                        get_unchanged_source_ranges(
                            source_range=source_range,
                            overlapping_ranges=overlapping_ranges,
                        )
                    )

    return get_sorted_ranges(ranges=destination_ranges)[0].start


def main() -> None:
    """Prints the solution to Day 5, Part Two."""

    lowest_location: float = inf
    lines: list[str] = read_puzzle_input(file_path=FILE_PATH)

    maps: list[list[ConversionMap]] = get_maps(lines=lines[1:])

    for seed_range in get_seed_ranges(line=lines[0]):
        location: int = get_min_location_for_seed_range(seed_range=seed_range, maps=maps)

        if location < lowest_location:
            lowest_location = location

    print(lowest_location)


if __name__ == "__main__":
    main()
