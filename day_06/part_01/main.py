from dataclasses import dataclass

FILE_PATH: str = "../puzzle_input.txt"


@dataclass
class Race:
    time: int
    distance: int


def get_races(lines: list[str]) -> list[Race]:
    """Returns a list of races.

    Args:
        lines: List of strings with race details

    Returns:
        List of races
    """

    times: list[int] = [int(time) for time in lines[0].split(":")[1].split()]
    distances: list[int] = [int(time) for time in lines[1].split(":")[1].split()]

    return [Race(time=times[i], distance=distances[i]) for i in range(len(times))]


def main() -> None:
    """Prints the solution to Day 6, Part One."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    for race in get_races(lines=lines):
        pass


if __name__ == "__main__":
    main()
