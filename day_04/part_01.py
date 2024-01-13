from day_04.common import separate_numbers

FILE: str = "puzzle_input.txt"


def get_points_for_card(winning_numbers: list[str], owned_numbers: list[str]) -> int:
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
    """Prints the solution to Day 4, Part One."""

    total: int = 0
    with open(file=FILE, mode="r") as file:
        lines: list[str] = [line.replace("\n", "") for line in file.readlines()]

    for line in lines:
        winning_numbers: list[str]
        owned_numbers: list[str]
        winning_numbers, owned_numbers = separate_numbers(numbers=line.split(":")[1])

        total += get_points_for_card(
            winning_numbers=winning_numbers,
            owned_numbers=owned_numbers,
        )

    print(total)


if __name__ == "__main__":
    main()
