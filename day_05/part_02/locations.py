from typing import Optional

from day_05.helpers import ConversionMap


class LowestLocationCalculator:
    """Class for calculating the lowest location number for a range of seed numbers.

    Attributes:
        source_ranges: List of source ranges (gets updated for each mapping, i.e. list of conversion maps)
        overlapping_ranges: List of ranges to be shifted (gets updated for each source range)
        destination_ranges: List of destination ranges (gets updated for each source range)
    """

    _instance: Optional["LowestLocationCalculator"] = None

    def __new__(cls, *args, **kwargs) -> "LowestLocationCalculator":
        if not cls._instance:
            cls._instance = super(LowestLocationCalculator, cls).__new__(cls)
        return cls._instance

    def __init__(self, seed_range: range) -> None:
        self.source_ranges: list[range] = []
        self.overlapping_ranges: list[range] = []
        self.destination_ranges: list[range] = [seed_range]

    def _is_full_overlap(self, source_range: range) -> bool:
        """Checks if there is a full overlap between the source range and one of the conversion map ranges.

        Args:
            source_range: Source range

        Returns:
            True in case of full overlap, False otherwise
        """

        return len(self.overlapping_ranges) == 1 and self.overlapping_ranges[0] == source_range

    def _get_unchanged_source_ranges(self, source_range: range) -> list[range]:
        """Returns a list of source ranges that had no overlap with any conversion map ranges.

        Args:
            source_range: Original source range

        Returns:
            Subsets of the original source range with no overlap
        """

        sorted_ranges: list[range] = self._get_sorted_ranges(ranges=self.overlapping_ranges)

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

    def _add_overlapping_range(self, source_range_start: int, range_length: int, shift: int) -> None:
        """Adds the new overlapping range to the lists of overlapping and destination ranges.

        Args:
            source_range_start: Source range start
            range_length: Source range length
            shift: Value by which to shift the overlapping range
        """

        # Add the overlapping part of the source range to overlapping ranges
        self.overlapping_ranges.append(
            range(
                source_range_start,
                source_range_start + range_length,
            )
        )
        # Add the shifted overlapping part of the source range to destination ranges
        self.destination_ranges.append(
            range(
                source_range_start + shift,
                source_range_start + shift + range_length,
            )
        )

    def _add_unchanged_ranges(self, source_range: range) -> None:
        """Adds unchanged subsets of the original source range to the list of destination ranges.

        Args:
            source_range: Original source range
        """

        if not self.overlapping_ranges:
            # Add the whole unchanged source range to destination ranges if there are no overlaps at all
            self.destination_ranges.append(
                range(
                    source_range.start,
                    source_range.stop,
                )
            )
        elif not self._is_full_overlap(source_range=source_range):
            # Full overlap between the source range and one of the conversion map ranges means that
            # there are no unchanged ranges to be added
            self.destination_ranges.extend(self._get_unchanged_source_ranges(source_range=source_range))

    def _update_destination_ranges(self, source_range: range, mapping: list[ConversionMap]) -> None:
        """Updates destination ranges.

        Args:
            source_range: Source range
            mapping: List of conversion maps
        """

        for conversion_map in mapping:
            conversion_map_range: range = range(
                conversion_map.source_range_start,
                conversion_map.source_range_start + conversion_map.range_length,
            )

            # Check if there's a full/partial overlap of ranges
            if self._ranges_overlap(source_range=source_range, conversion_map_range=conversion_map_range):
                source_range_start, range_length = self._get_range_parameters(
                    source_range=source_range,
                    conversion_map_range=conversion_map_range,
                )

                self._add_overlapping_range(
                    source_range_start=source_range_start,
                    range_length=range_length,
                    shift=conversion_map.destination_range_start - conversion_map.source_range_start,
                )

        self._add_unchanged_ranges(source_range=source_range)

    def get_location(self, maps: list[list[ConversionMap]]) -> int:
        """Returns the lowest location number for a range of seed numbers.

        Args:
            maps: List of conversion mappings

        Returns:
            Location number
        """

        for mapping in maps:
            self.source_ranges = self.destination_ranges.copy()
            self.destination_ranges.clear()
            for source_range in self.source_ranges:
                self.overlapping_ranges.clear()
                self._update_destination_ranges(source_range=source_range, mapping=mapping)

        return self._get_sorted_ranges(ranges=self.destination_ranges)[0].start

    @staticmethod
    def _ranges_overlap(source_range: range, conversion_map_range: range) -> bool:
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

    @staticmethod
    def _get_range_parameters(source_range: range, conversion_map_range: range) -> tuple[int, int]:
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

    @staticmethod
    def _get_sorted_ranges(ranges: list[range]) -> list[range]:
        """Sorts ranges by their start in ascending order.

        Args:
            ranges: List of ranges

        Returns:
            Sorted ranges
        """

        return sorted(ranges, key=lambda r: r.start)
