from common import get_loop_positions, Position, get_max_steps

FILE: str = "puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 10, Part One."""

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

    print(get_max_steps(positions=positions))


if __name__ == "__main__":
    main()
