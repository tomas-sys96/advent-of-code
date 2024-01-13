from day_02.common import are_cube_amounts_possible

FILE: str = "puzzle_input.txt"

max_cube_amount: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main() -> None:
    """Prints the solution to Day 2, Part One."""

    total: int = 0
    with open(file=FILE, mode="r") as file:
        lines: list[str] = [line.replace("\n", "") for line in file.readlines()]

    for line in lines:
        # cube_sets = ['10 green', '9 blue', '1 red', '7 green', ...]
        cube_sets: list[str] = line.split(":")[1].replace("\n", "").replace(";", ",").split(",")

        if are_cube_amounts_possible(cube_sets=cube_sets, max_cube_amount=max_cube_amount):
            total += int(line.split(":")[0].split()[1])

    print(total)


if __name__ == "__main__":
    main()
