FILE_PATH: str = "../puzzle_input.txt"

max_cube_amount_per_color: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_too_many_cubes(cube_amount: int, cube_color: str) -> bool:
    """Checks if a cube amount doesn't exceed its limit for a given color.

    Args:
        cube_amount: Amount of cubes
        cube_color: Color of the cube

    Returns:
        True if the cube amount doesn't exceed a limit, False otherwise
    """

    return cube_amount > max_cube_amount_per_color[cube_color]


def are_cube_amounts_possible(cube_subsets: list[str]) -> bool:
    """Checks if all the amounts of cubes are possible for a given game.

    Args:
        cube_subsets: Cube subsets (e.g. ['10 green, 9 blue', '1 red, 7 green'])

    Returns:
        True if all the cube amount are possible, False otherwise
    """

    for cube_subset in cube_subsets:
        for cube in cube_subset.split(","):
            cube_amount: int = int(cube.split()[0].strip())
            cube_color: str = cube.split()[1].strip()
            if is_too_many_cubes(cube_amount=cube_amount, cube_color=cube_color):
                return False

    return True


def main() -> None:
    """Prints the sum of IDs of games that would have been possible, given the number of cubes in the bag."""

    game_ids_sum: int = 0

    with open(file=FILE_PATH, mode="r") as file:
        while True:
            # Read and process lines one by one
            line: str = file.readline()
            # Break the loop if there are no more lines
            if not line:
                break

            cube_subsets: list[str] = line.split(":")[1].replace("\n", "").strip().split(";")

            if are_cube_amounts_possible(cube_subsets=cube_subsets):
                game_ids_sum += int(line.split(":")[0].split()[1])

    print(game_ids_sum)


if __name__ == "__main__":
    main()
