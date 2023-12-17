from day_04.helpers import separate_numbers

FILE_PATH: str = "../puzzle_input.txt"


class Card:
    """"""

    def __init__(self, number: int, winning_numbers: list[int], owned_numbers: list[int]) -> None:
        self.number: int = number
        self.winning_numbers: list[int] = winning_numbers
        self.owned_numbers: list[int] = owned_numbers
        self.points: int = 0

    def get_points_for_card(self) -> None:
        """"""

        for number in self.owned_numbers:
            if number in self.winning_numbers:
                self.points += 1

    def get_next_card_numbers(self) -> list[int]:
        """"""

        self.get_points_for_card()
        return list(range(self.number + 1, self.number + self.points + 1))


def main() -> None:
    """Prints the sum of all original and copied winning scratchcards."""

    card_instances: dict[str, int] = {}

    with open(file=FILE_PATH, mode="r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break

            current_card_number: int = int(line.split(":")[0].split()[1].strip())
            # At least one instance of each of the original scratchcards is always included
            if f"card_{current_card_number}" in card_instances.keys():
                card_instances[f"card_{current_card_number}"] += 1
            else:
                card_instances[f"card_{current_card_number}"] = 1

            card: Card = Card(
                current_card_number,
                *separate_numbers(numbers=line.split(":")[1]),
            )

            next_card_numbers: list[int] = card.get_next_card_numbers()
            for number in next_card_numbers:
                try:
                    card_instances[f"card_{number}"] += card_instances[f"card_{current_card_number}"]
                except KeyError:
                    card_instances[f"card_{number}"] = card_instances[f"card_{current_card_number}"]

    print(sum(card_instances.values()))


if __name__ == "__main__":
    main()
