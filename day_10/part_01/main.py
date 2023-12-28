from collections import namedtuple
from enum import StrEnum

FILE_PATH: str = "../puzzle_input.txt"

Shift: namedtuple = namedtuple(typename="Shift", field_names=["line", "position", "direction"])


class Direction(StrEnum):
    NORTH: str = "north"
    SOUTH: str = "south"
    EAST: str = "east"
    WEST: str = "west"


def find_highest_number_of_steps_along_loop(
    pipes: dict[str, dict[Direction, Shift]],
    lines: list[str],
    line: int,
    position: int,
    direction: Direction,
) -> int:
    """Returns the highest number of steps along a closed loop.

    Args:
        pipes: Pipe symbols mapping (line step, position step and direction)
        lines: List of lines
        line: Index of the line in lines
        position: Index of the character in the line
        direction: Direction in which to continue

    Returns:
        Highest number of steps along the loop
    """

    character: str = lines[line][position]

    steps: int = 0
    while True:
        steps += 1

        try:
            shift: Shift = pipes[character][direction]
            line += shift.line
            position += shift.position
            direction = shift.direction
        except KeyError:
            if character == ".":
                return 0
            return int(steps / 2)

        character = lines[line][position]


def main() -> None:
    """Prints the solution to Day 10, Part One."""

    pipes: dict[str, dict[Direction, Shift]] = {
        "|": {
            Direction.NORTH: Shift(line=-1, position=0, direction=Direction.NORTH),
            Direction.SOUTH: Shift(line=1, position=0, direction=Direction.SOUTH),
        },
        "-": {
            Direction.EAST: Shift(line=0, position=1, direction=Direction.EAST),
            Direction.WEST: Shift(line=0, position=-1, direction=Direction.WEST),
        },
        "L": {
            Direction.SOUTH: Shift(line=0, position=1, direction=Direction.EAST),
            Direction.WEST: Shift(line=-1, position=0, direction=Direction.NORTH),
        },
        "J": {
            Direction.SOUTH: Shift(line=0, position=-1, direction=Direction.WEST),
            Direction.EAST: Shift(line=-1, position=0, direction=Direction.NORTH),
        },
        "7": {
            Direction.NORTH: Shift(line=0, position=-1, direction=Direction.WEST),
            Direction.EAST: Shift(line=1, position=0, direction=Direction.SOUTH),
        },
        "F": {
            Direction.NORTH: Shift(line=0, position=1, direction=Direction.EAST),
            Direction.WEST: Shift(line=1, position=0, direction=Direction.SOUTH),
        },
    }

    number_of_steps: list[int] = []

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    starting_line: int = 0
    starting_position: int = 0

    for line_index, line in enumerate(lines):
        if "S" in line:
            starting_line = line_index
            starting_position = line.index("S")

    # Starting directions: north and south
    for line_step in [-1, 1]:
        number_of_steps.append(
            find_highest_number_of_steps_along_loop(
                pipes=pipes,
                lines=lines,
                line=starting_line + line_step,
                position=starting_position,
                direction=Direction.NORTH if line_step == -1 else Direction.SOUTH,
            )
        )

    # Starting directions: west and east
    for index_step in [-1, 1]:
        number_of_steps.append(
            find_highest_number_of_steps_along_loop(
                pipes=pipes,
                lines=lines,
                line=starting_line,
                position=starting_position + index_step,
                direction=Direction.WEST if index_step == -1 else Direction.EAST,
            )
        )

    print(max(number_of_steps))


if __name__ == "__main__":
    main()
