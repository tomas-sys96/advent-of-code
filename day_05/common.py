from collections import namedtuple

ConversionMap: namedtuple = namedtuple(
    typename="ConversionMap",
    field_names=[
        "destination_range_start",
        "source_range_start",
        "range_length",
    ],
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
