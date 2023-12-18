from collections import namedtuple
from math import inf

from common import read_puzzle_input

ConversionRange: namedtuple = namedtuple(
    typename="ConversionRange",
    field_names=[
        "destination_range_start",
        "source_range_start",
        "range_length",
    ],
)


def get_seeds(line: str) -> list[int]:
    """Returns the seed numbers (initial source numbers).

    Args:
        line: String with info about the ranges of seed numbers

    Returns:
        List of seed numbers
    """

    source_ranges: list[int] = [int(number) for number in line.split(":")[1].split()]

    for number_index in range(0, len(source_ranges), 2):
        range_start: int = source_ranges[number_index]
        range_length = source_ranges[number_index + 1]
        for seed in range(range_start, range_start + range_length):
            yield seed


def get_destination(source: int, conversion_ranges: list[ConversionRange]) -> int:
    """Converts a source number to a destination number.

    Args:
        source: Source number
        conversion_ranges: List of conversion ranges

    Returns:
        destination: Destination number
    """

    for conversion in conversion_ranges:
        if source in range(conversion.source_range_start, conversion.source_range_start + conversion.range_length):
            return conversion.destination_range_start + (source - conversion.source_range_start)

    return source


def main() -> None:
    """Prints the solution to Day 5, Part Two."""

    lowest_location_number: float = inf
    lines: list[str] = read_puzzle_input()
    # Append an empty string to the lines so that the last source-destination conversion may trigger
    lines.append("")

    for seed in get_seeds(line=lines[0]):
        source: int = seed
        conversion_ranges: list[ConversionRange] = []

        # Start on the first line of numbers of the seed-to-soil map
        for line in lines[3:]:
            if not line:
                # Convert a source to a destination
                source = get_destination(source=source, conversion_ranges=conversion_ranges)

                # Empty the list and continue on the next line
                conversion_ranges.clear()
                continue

            # Ignore lines without numbers
            if any([character.isalpha() for character in line]):
                continue

            destination_range_start: int
            source_range_start: int
            range_length: int
            destination_range_start, source_range_start, range_length = [int(number) for number in line.split()]

            # TODO: The destination number could be calculated here, as soon as the source is within the range
            #  -> convert to destination
            #  -> no need for conversion_ranges list

            conversion_ranges.append(
                ConversionRange(
                    destination_range_start,
                    source_range_start,
                    range_length,
                )
            )

        if source < lowest_location_number:
            lowest_location_number = source

    print(lowest_location_number)


if __name__ == "__main__":
    main()
