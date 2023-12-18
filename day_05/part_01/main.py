from math import inf

from day_05.helpers import read_puzzle_input, get_maps, get_location, ConversionRange


def main() -> None:
    """Prints the solution to Day 5, Part One."""

    lowest_location: float = inf
    lines: list[str] = read_puzzle_input()

    maps: list[list[ConversionRange]] = get_maps(lines=lines[1:])
    seeds: list[int] = [int(number) for number in lines[0].split(":")[1].split()]

    for seed in seeds:
        location: int = get_location(seed=seed, maps=maps)

        if location < lowest_location:
            lowest_location = location

    print(lowest_location)


if __name__ == "__main__":
    main()
