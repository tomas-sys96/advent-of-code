from day_04.common import separate_numbers

FILE_PATH: str = "../puzzle_input.txt"


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
            points += 1

    return points


def main() -> None:
    """Prints the solution to Day 4, Part Two."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = [line.replace("\n", "") for line in file.readlines()]

    card_instances: dict[str, int] = {}

    for line in lines:
        card_number: int = int(line.split(":")[0].split()[1].strip())

        # One instance of each of the original scratchcards is always included
        try:
            card_instances[f"card_{card_number}"] += 1
        except KeyError:
            card_instances[f"card_{card_number}"] = 1

        winning_numbers: list[str]
        owned_numbers: list[str]
        winning_numbers, owned_numbers = separate_numbers(numbers=line.split(":")[1])

        points: int = get_points_for_card(winning_numbers=winning_numbers, owned_numbers=owned_numbers)
        for number in range(card_number + 1, min(card_number + points, len(lines)) + 1):
            try:
                card_instances[f"card_{number}"] += card_instances[f"card_{card_number}"]
            except KeyError:
                card_instances[f"card_{number}"] = card_instances[f"card_{card_number}"]

    print(sum(card_instances.values()))


if __name__ == "__main__":
    main()
