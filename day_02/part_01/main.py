from dataclasses import dataclass
from common import read_file

FILE_PATH: str = "../puzzle_input.txt"

max_cube_amount_per_color: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_too_many_cubes(cube_amount: int, cube_color: str) -> bool:
    """"""

    return cube_amount > max_cube_amount_per_color[cube_color]


def is_cube_amount_possible(cube_subsets: list[str]) -> bool:
    """"""

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
            if not line:
                break

            cube_subsets: list[str] = line.split(":")[1].replace("\n", "").strip().split(";")

            if is_cube_amount_possible(cube_subsets=cube_subsets):
                game_ids_sum += int(line.split(":")[0].split()[1])

    print(game_ids_sum)


if __name__ == "__main__":
    main()
