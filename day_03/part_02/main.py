from day_03.common import read_file
from symbol_detector import SymbolDetector


FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    """Prints the sum of all the gear ratios in the engine schematic."""

    lines: list[str] = read_file(file_path=FILE_PATH)

    gear_ratios_sum: int = 0
    digits: list[str] = []


if __name__ == "__main__":
    main()
