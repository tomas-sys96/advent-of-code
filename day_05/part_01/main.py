from common import read_puzzle_input


def main() -> None:
    """Prints the solution to Day 5, Part One."""

    lines: list[str] = read_puzzle_input()
    seeds: list[int] = [int(number) for number in lines[0].split(":")[1].split()]

    source_to_destination: dict = {}

    # Start on the first line of numbers of the seed-to-soil map
    for line in lines[3:]:
        if not line:
            # Time to convert source to destination
            pass

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


if __name__ == "__main__":
    main()
