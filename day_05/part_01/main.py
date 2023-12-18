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


def main() -> None:
    """Prints the solution to Day 5, Part One."""

    lines: list[str] = read_puzzle_input()
    # Append an empty string to the lines so that the last source-destination conversion may trigger
    lines.append("")

    sources: list[int] = [int(number) for number in lines[0].split(":")[1].split()]
    destinations: list[int] = sources.copy()

    conversion_ranges: list[ConversionRange] = []

    # Start on the first line of numbers of the seed-to-soil map
    for line in lines[3:]:
        if not line:
            # Convert sources to destinations
            for source_index, source in enumerate(sources):
                for conversion in conversion_ranges:
                    if source in range(
                        conversion.source_range_start, conversion.source_range_start + conversion.range_length
                    ):
                        destination: int = conversion.destination_range_start + (source - conversion.source_range_start)
                        destinations[source_index] = destination
                        break

            sources = destinations.copy()

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

    # print(min(destinations))


if __name__ == "__main__":
    # main()
    from timeit import timeit

    print(f"{timeit(main, number=2000)} s")
