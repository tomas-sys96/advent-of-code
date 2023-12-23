from dataclasses import dataclass
from math import prod

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


def get_record_beats(race: Race) -> int:
    """Returns the number of ways that one can beat the record in a race.

    Args:
        race: Race

    Returns:
        record_beats: Number of ways to beat the record
    """

    record_beats: int = 0
    for charge_time in range(1, race.time):
        distance: int = charge_time * (race.time - charge_time)
        if distance > race.distance:
            record_beats += 1

    return record_beats


def main() -> None:
    """Prints the solution to Day 6, Part One."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    record_beats_per_race: list[int] = []

    for race in get_races(lines=lines):
        record_beats_per_race.append(get_record_beats(race=race))

    print(prod(record_beats_per_race))


if __name__ == "__main__":
    main()
