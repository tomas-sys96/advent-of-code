from math import sqrt, ceil, floor

from common import Race

FILE: str = "puzzle_input.txt"


def get_race(lines: list[str]) -> Race:
    """Returns race info.

    Args:
        lines: List of strings with race details

    Returns:
        Race
    """

    time: int = int("".join(lines[0].split(":")[1].split()))
    distance: int = int("".join(lines[1].split(":")[1].split()))

    return Race(time=time, distance=distance)


def solve_quadratic_equation(a: int, b: int, c: int) -> tuple[float, float]:
    """Returns roots of a quadratic equation specified by coefficients.

    Args:
        a: Coefficient
        b: Coefficient
        c: Coefficient

    Returns:
        tuple:
            x_1: Root,
            x_2: Root
    """

    discriminant: int = (-b) ** 2 - 4 * a * c
    x_1: float = (-b + sqrt(discriminant)) / (2 * a)
    x_2: float = (-b - sqrt(discriminant)) / (2 * a)

    return x_1, x_2


def main() -> None:
    """Prints the solution to Day 6, Part Two."""

    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.readlines()

    race: Race = get_race(lines=lines)

    # race.distance + 1 = charge_time * (race.time - charge_time)
    # charge_time * 2 - charge_time * race.time + race.distance + 1
    charge_times: tuple[float, float]
    charge_times = solve_quadratic_equation(a=1, b=-race.time, c=race.distance + 1)

    charge_time_min: int = ceil(min(charge_times))
    charge_time_max: int = floor(max(charge_times))

    print(charge_time_max - charge_time_min + 1)


if __name__ == "__main__":
    main()
