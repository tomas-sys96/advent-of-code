from day_04.helpers import separate_numbers
from day_04.part_02.card import Card

FILE_PATH: str = "../puzzle_input.txt"


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
            for card_number in next_card_numbers:
                try:
                    card_instances[f"card_{card_number}"] += card_instances[f"card_{current_card_number}"]
                except KeyError:
                    card_instances[f"card_{card_number}"] = card_instances[f"card_{current_card_number}"]

            # Delete the card object from memory
            del card

    print(sum(card_instances.values()))


if __name__ == "__main__":
    main()
