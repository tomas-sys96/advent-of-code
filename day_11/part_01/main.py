from day_11.common import SpaceExpansionCalculator

FILE_PATH: str = "../puzzle_input.txt"


def main() -> None:
    with open(file=FILE_PATH, mode="r") as file:
        rows: list[str] = file.readlines()

    space_expansion_calculator: SpaceExpansionCalculator = SpaceExpansionCalculator(
        rows=rows,
        expanded_space_distance=1,
        expansion_multiplies=False,
    )
    print(space_expansion_calculator.get_distance_between_galaxies())


if __name__ == "__main__":
    main()
