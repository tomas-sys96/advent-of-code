from math import prod

FILE_PATH: str = "../puzzle_input.txt"


def get_min_number_of_cubes_per_color(cube_sets: list[str]) -> dict[str, int]:
    """Creates a dictionary with the fewest number of cubes of each color that could have been in the bag.

    Args:
        cube_sets: List of strings with cube amounts and colors

    Returns:
        Dictionary with minimum number of cubes per color
    """

    cubes_per_color: dict[str, int] = {}

    for cube_set in cube_sets:
        cube_amount: int = int(cube_set.split()[0].strip())
        cube_color: str = cube_set.split()[1].strip()

        try:
            if cube_amount > cubes_per_color[cube_color]:
                cubes_per_color[cube_color] = cube_amount
        except KeyError:
            cubes_per_color[cube_color] = cube_amount

    return cubes_per_color


def main() -> None:
    """Prints the sum of the power of the minimum sets of cubes per game."""

    power_sum: int = 0

    with open(file=FILE_PATH, mode="r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break

            # cube_sets = ['10 green', '9 blue', '1 red', '7 green', ...]
            cube_sets: list[str] = line.split(":")[1].replace("\n", "").replace(";", ",").split(",")

            cubes_per_color: dict[str, int] = get_min_number_of_cubes_per_color(cube_sets=cube_sets)
            power_sum += prod(cubes_per_color.values())

    print(power_sum)


if __name__ == "__main__":
    main()
