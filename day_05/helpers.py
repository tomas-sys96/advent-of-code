import sys
from collections import namedtuple

ConversionRange: namedtuple = namedtuple(
    typename="ConversionRange",
    field_names=[
        "destination_range_start",
        "source_range_start",
        "range_length",
    ],
)


def read_puzzle_input(file_path: str) -> list[str]:
    """Reads a puzzle input text file located in the root of the current directory.

    Args:
        Puzzle input file path

    Returns:
        Text file represented as a list of strings
    """

    try:
        with open(file=file_path, mode="r") as file:
            return file.read().split("\n\n")
    except FileNotFoundError as exception:
        sys.exit(
            f"{exception.__class__.__name__}: "
            f"Puzzle input text file is missing in the root of the day_XY/ directory"
        )


def get_maps(lines: list[str]) -> list[list[ConversionRange]]:
    """Returns the conversion maps.

    Args:
        lines: Lists of strings containing conversion maps details

    Returns:
        maps: List of conversion maps lists
    """

    maps: list[list[ConversionRange]] = []
    for conversion_map in lines:
        map_to_bind: list[ConversionRange] = []
        for conversion_range in conversion_map.split("\n")[1:]:
            if not conversion_range:
                continue
            map_to_bind.append(ConversionRange(*[int(number) for number in conversion_range.split()]))
        maps.append(map_to_bind)

    return maps


def get_location(seed: int, maps: list[list[ConversionRange]]) -> int:
    """Converts a seed number to a location number.

    Args:
        seed: Seed number
        maps: List of conversion maps

    Returns:
        value: Location number
    """

    value: int = seed

    for conversion_map in maps:
        for conversion in conversion_map:
            if value in range(conversion.source_range_start, conversion.source_range_start + conversion.range_length):
                value = conversion.destination_range_start + (value - conversion.source_range_start)
                break

    return value
