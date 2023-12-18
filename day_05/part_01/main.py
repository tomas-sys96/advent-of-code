from common import read_puzzle_input


def main() -> None:
    """Prints the solution to Day 5, Part One."""

    lines: list[str] = read_puzzle_input()
    sources: list[int] = [int(number) for number in lines[0].split(":")[1].split()]
    destinations: list[int] = sources.copy()

    source_to_destination: dict = {}

    # Start on the first line of numbers of the seed-to-soil map
    for line in lines[3:]:
        if not line:
            # Convert sources to destinations
            for source_index, source in enumerate(sources):
                destination: int
                try:
                    destination = source_to_destination[source]
                except KeyError:
                    destination = source

                destinations[source_index] = destination
                sources = destinations.copy()

            # Empty the dictionary and continue on the next line
            source_to_destination.clear()
            continue

        # Ignore lines without numbers
        if any([character.isalpha() for character in line]):
            continue

        destination_range_start: int
        source_range_start: int
        range_length: int
        destination_range_start, source_range_start, range_length = [int(number) for number in line.split()]

        for step in range(range_length):
            try:
                source_to_destination[source_range_start + step] = source_to_destination[source_range_start] + step
            except KeyError:
                source_to_destination[source_range_start] = destination_range_start

    print(min(destinations))


if __name__ == "__main__":
    main()
