from math import prod

from common import get_min_number_of_cubes_per_color

FILE: str = "puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 2, Part Two."""

    total: int = 0
    with open(file=FILE, mode="r") as file:
        lines: list[str] = [line.replace("\n", "") for line in file.readlines()]

    for line in lines:
        # cube_sets = ['10 green', '9 blue', '1 red', '7 green', ...]
        cube_sets: list[str] = line.split(":")[1].replace("\n", "").replace(";", ",").split(",")

        cubes_per_color: dict[str, int] = get_min_number_of_cubes_per_color(cube_sets=cube_sets)
        total += prod(cubes_per_color.values())

    print(total)


if __name__ == "__main__":
    main()
