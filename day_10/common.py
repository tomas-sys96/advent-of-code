from collections import namedtuple
from enum import StrEnum

Shift: namedtuple = namedtuple(typename="Shift", field_names=["line", "char_index", "direction"])
Position: namedtuple = namedtuple(typename="Position", field_names=["line", "char_index"])


class Direction(StrEnum):
    NORTH: str = "north"
    SOUTH: str = "south"
    EAST: str = "east"
    WEST: str = "west"


pipes_and_bends: dict[str, dict[Direction, Shift]] = {
    "|": {
        Direction.NORTH: Shift(
            line=-1,
            char_index=0,
            direction=Direction.NORTH,
        ),
        Direction.SOUTH: Shift(
            line=1,
            char_index=0,
            direction=Direction.SOUTH,
        ),
    },
    "-": {
        Direction.EAST: Shift(
            line=0,
            char_index=1,
            direction=Direction.EAST,
        ),
        Direction.WEST: Shift(
            line=0,
            char_index=-1,
            direction=Direction.WEST,
        ),
    },
    "L": {
        Direction.SOUTH: Shift(
            line=0,
            char_index=1,
            direction=Direction.EAST,
        ),
        Direction.WEST: Shift(
            line=-1,
            char_index=0,
            direction=Direction.NORTH,
        ),
    },
    "J": {
        Direction.SOUTH: Shift(
            line=0,
            char_index=-1,
            direction=Direction.WEST,
        ),
        Direction.EAST: Shift(
            line=-1,
            char_index=0,
            direction=Direction.NORTH,
        ),
    },
    "7": {
        Direction.NORTH: Shift(
            line=0,
            char_index=-1,
            direction=Direction.WEST,
        ),
        Direction.EAST: Shift(
            line=1,
            char_index=0,
            direction=Direction.SOUTH,
        ),
    },
    "F": {
        Direction.NORTH: Shift(
            line=0,
            char_index=1,
            direction=Direction.EAST,
        ),
        Direction.WEST: Shift(
            line=1,
            char_index=0,
            direction=Direction.SOUTH,
        ),
    },
}


def get_next_line_and_char_index(line: int, char_index: int, direction: Direction) -> tuple[int, int]:
    """Returns the next line and character index based on a direction.

    Args:
        line: Current line
        char_index: Current character index
        direction: Direction

    Returns:
        tuple:
            line: Next line,
            char_index: Next character index
    """

    match direction:
        case Direction.NORTH:
            line -= 1
        case Direction.SOUTH:
            line += 1
        case Direction.WEST:
            char_index -= 1
        case _:
            char_index += 1

    return line, char_index


def find_loop_positions_in_direction(
    lines: list[str],
    starting_line: int,
    starting_char_index: int,
    direction: Direction,
) -> list[Position]:
    """Returns a list of positions creating a loop, starting in a given direction.

    Args:
        lines: List of lines
        starting_line: Starting line
        starting_char_index: Starting character index
        direction: Starting direction

    Returns:
        positions: List of loop positions
    """

    # Initialize the positions with the starting position
    positions: list[Position] = [Position(line=starting_line, char_index=starting_char_index)]

    # Get next position based on the starting direction
    line: int
    char_index: int
    line, char_index = get_next_line_and_char_index(
        line=starting_line,
        char_index=starting_char_index,
        direction=direction,
    )

    while True:
        character: str = lines[line][char_index]

        try:
            shift: Shift = pipes_and_bends[character][direction]
        except KeyError:
            # Either the starting position has been reached ("S"), or the ground (".")
            if character == "S":
                return positions
            return []

        positions.append(Position(line=line, char_index=char_index))

        line += shift.line
        char_index += shift.char_index
        direction = shift.direction


def get_loop_positions(lines: list[str], starting_line: int, starting_char_index: int) -> list[Position]:
    """Returns a list of positions creating a loop.

    Args:
        lines: List of lines
        starting_line: Starting line
        starting_char_index: Starting character index

    Returns:
        positions: List of loop positions
    """

    directions: list[Direction] = [Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST]
    for direction in directions:
        positions: list[Position] = find_loop_positions_in_direction(
            lines=lines,
            starting_line=starting_line,
            starting_char_index=starting_char_index,
            direction=direction,
        )
        if positions:
            return positions

    return []


def get_max_steps(positions: list[Position]) -> int:
    """Returns the number of steps that it takes to get to the farthest loop position.

    Args:
        positions: List of loop positions

    Returns:
        Number of steps to the farthest loop position
    """

    return int(len(positions) / 2)


def get_loop_area(positions: list[Position]) -> int:
    """Returns a loop area.

    Args:
        positions: List of loop positions

    Returns:
        Loop area
    """

    area: int = 0

    for i in range(len(positions)):
        position: Position = positions[i]
        next_position: Position

        try:
            next_position = positions[i + 1]
        except IndexError:
            next_position = positions[0]

        # Trapezoid/shoelace formula
        area += 0.5 * (position.line + next_position.line) * (position.char_index - next_position.char_index)

    return int(abs(area))


def get_number_of_enclosed_tiles(positions: list[Position]) -> int:
    """Returns the number of tiles enclosed by the loop.

    Args:
        positions: List of loop positions

    Returns:
        Number of enclosed tiles
    """

    # Pick's theorem
    # A = i + b / 2 - 1
    return int(get_loop_area(positions=positions) - len(positions) / 2 + 1)
