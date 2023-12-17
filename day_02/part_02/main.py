from math import prod

FILE_PATH: str = "../puzzle_input.txt"


def get_min_number_of_cubes_per_color(cube_subsets: list[str]) -> dict[str, int]:
    """Creates a dictionary with the fewest number of cubes of each color that could have been in the bag.

    Args:
        cube_subsets: Cube subsets (e.g. ['10 green, 9 blue', '1 red, 7 green'])

    Returns:
        Dictionary with minimum number of cubes per color
    """

    cubes_per_color: dict[str, int] = {}

    for cube_subset in cube_subsets:
        for cube in cube_subset.split(","):
            cube_amount: int = int(cube.split()[0].strip())
            cube_color: str = cube.split()[1].strip()

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

            # cube_subsets = ['10 green, 9 blue', '1 red, 7 green', ...]
            cube_subsets: list[str] = line.split(":")[1].replace("\n", "").strip().split(";")

            cubes_per_color: dict[str, int] = get_min_number_of_cubes_per_color(cube_subsets=cube_subsets)
            power_sum += prod(cubes_per_color.values())

    print(power_sum)


if __name__ == "__main__":
    main()
