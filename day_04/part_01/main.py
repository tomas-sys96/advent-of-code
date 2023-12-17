from day_04.helpers import separate_numbers

FILE_PATH: str = "../puzzle_input.txt"


def get_points_for_card(winning_numbers: list[int], owned_numbers: list[int]) -> int:
    """Calculates the points for a card.

    Args:
        winning_numbers: Winning numbers
        owned_numbers: Numbers that a person owns

    Returns:
        Points for a card
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
    total: int = 0

    with open(file=FILE_PATH, mode="r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break

            winning_numbers: list[int]
            owned_numbers: list[int]
            winning_numbers, owned_numbers = separate_numbers(numbers=line.split(":")[1])

            total += get_points_for_card(
                winning_numbers=winning_numbers,
                owned_numbers=owned_numbers,
            )

    print(total)


if __name__ == "__main__":
    main()
