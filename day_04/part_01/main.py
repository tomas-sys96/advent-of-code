from day_04.helpers import separate_numbers

FILE_PATH: str = "../puzzle_input.txt"


def get_points_for_card(winning_numbers: list[int], owned_numbers: list[int]) -> int:
    """Calculates the sum of points per one card.

    Args:
        winning_numbers: Winning numbers
        owned_numbers: Numbers that a person owns

    Returns:
        Points per one card
    """

    points: int = 0
    for number in owned_numbers:
        if number in winning_numbers:
            if points:
                points *= 2
            else:
                points += 1

    return points


def main() -> None:
    """Prints the points sum of a pile of scratchcards."""

    scratchcard_points_sum: int = 0

    with open(file=FILE_PATH, mode="r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break

            winning_numbers: list[int]
            owned_numbers: list[int]
            winning_numbers, owned_numbers = separate_numbers(numbers=line.split(":")[1])

            scratchcard_points_sum += get_points_for_card(
                winning_numbers=winning_numbers,
                owned_numbers=owned_numbers,
            )

    print(scratchcard_points_sum)


if __name__ == "__main__":
    main()
