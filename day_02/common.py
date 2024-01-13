def are_cube_amounts_possible(cube_sets: list[str], max_cube_amount: dict[str, int]) -> bool:
    """Checks if all the amounts of cubes are possible for a given game.

    Args:
        cube_sets: List of strings with cube amounts and colors
        max_cube_amount: Maximum amount of cubes per color

    Returns:
        True if all the cube amount are possible, False otherwise
    """

    for cube_set in cube_sets:
        cube_amount: int = int(cube_set.split()[0].strip())
        cube_color: str = cube_set.split()[1].strip()
        if cube_amount > max_cube_amount[cube_color]:
            return False

    return True


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
