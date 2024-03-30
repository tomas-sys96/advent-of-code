from common import get_loop_positions, Position, get_number_of_enclosed_tiles

FILE: str = "puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 10, Part Two."""

    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.readlines()

    starting_line: int = 0
    starting_index: int = 0

    for line_index, line in enumerate(lines):
        if "S" in line:
            starting_line = line_index
            starting_index = line.index("S")

    positions: list[Position] = get_loop_positions(
        lines=lines,
        starting_line=starting_line,
        starting_char_index=starting_index,
    )

    print(get_number_of_enclosed_tiles(positions=positions))


if __name__ == "__main__":
    main()
