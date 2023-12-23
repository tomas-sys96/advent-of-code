import sys
from collections import namedtuple

ConversionMap: namedtuple = namedtuple(
    typename="ConversionMap",
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


def get_maps(lines: list[str]) -> list[list[ConversionMap]]:
    """Returns a list of conversion mappings.

    Args:
        lines: Lists of strings with source-to-destination mappings

    Returns:
        maps: List of conversion mappings
    """

    maps: list[list[ConversionMap]] = []
    for mapping in lines:
        conversion_maps: list[ConversionMap] = []
        for conversion_map in mapping.split("\n")[1:]:
            if not conversion_map:
                continue
            conversion_maps.append(ConversionMap(*[int(number) for number in conversion_map.split()]))
        maps.append(conversion_maps)

    return maps
