from collections import namedtuple

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
    # Here, we're using a set object to avoid duplicate seed numbers
    seeds: set[int] = set()

    for number_index in range(0, len(source_ranges), 2):
        range_start: int = source_ranges[number_index]
        range_length = source_ranges[number_index + 1]
        seeds.update(set(range(range_start, range_start + range_length)))

    return list(seeds)


def get_destinations(sources: list[int], conversion_ranges: list[ConversionRange]) -> list[int]:
    """Converts sources to destinations.

    Args:
        sources: List of source numbers
        conversion_ranges: List of conversion ranges

    Returns:
        destinations: List of destination numbers
    """

    # Here, we're using a set object to avoid duplicate destination numbers
    destinations: set[int] = set()

    for source in sources:
        is_converted: bool = False
        for conversion in conversion_ranges:
            if source in range(conversion.source_range_start, conversion.source_range_start + conversion.range_length):
                destination: int = conversion.destination_range_start + (source - conversion.source_range_start)
                destinations.add(destination)
                is_converted = True
                break
        if not is_converted:
            destinations.add(source)

    return list(destinations)


def main() -> None:
    """Prints the solution to Day 5, Part Two."""

    lines: list[str] = read_puzzle_input()
    # Append an empty string to the lines so that the last source-destination conversion may trigger
    lines.append("")

    sources: list[int] = get_seeds(line=lines[0])
    conversion_ranges: list[ConversionRange] = []

    # Start on the first line of numbers of the seed-to-soil map
    for line in lines[3:]:
        if not line:
            # Convert sources to destinations (i.e. sources for the next conversion)
            sources = get_destinations(sources=sources, conversion_ranges=conversion_ranges)

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

        conversion_ranges.append(
            ConversionRange(
                destination_range_start,
                source_range_start,
                range_length,
            )
        )

    print(min(sources))


if __name__ == "__main__":
    main()
