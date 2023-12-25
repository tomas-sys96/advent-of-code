from dataclasses import dataclass
from collections import defaultdict

FILE_PATH: str = "../puzzle_input.txt"


@dataclass
class Hand:
    cards: str
    bid: int
    strength: int


def get_strength_of_hand(cards: str, mapping: dict[str, int]) -> int:
    """Returns the strength of a hand based on its type.

    Args:
        cards: String of card labels
        mapping: Type to strength mapping

    Returns:
        Strength value
    """

    label_count: defaultdict = defaultdict(int)

    for label in cards:
        label_count[label] += 1

    match len(label_count):
        case 1:
            return mapping["five_of_kind"]
        case 2:
            if any([count == 4 for count in label_count.values()]):
                return mapping["four_of_kind"]
            else:
                return mapping["full_house"]
        case 3:
            if any([count == 3 for count in label_count.values()]):
                return mapping["three_of_kind"]
            else:
                return mapping["two_pairs"]
        case 4:
            return mapping["one_pair"]
        case _:
            return mapping["high_card"]


def sort_by_strength_and_labels(hand: Hand, mapping: dict[str, int]) -> tuple[int, tuple]:
    """Sorts hands of cards primarily based on their strength, and secondarily based on the order of individual labels.

    Args:
        hand: Hand of cards
        mapping: Label to order mapping

    Returns:
        tuple:
            Hand strength -- first rule,
            Label order -- second rule
    """

    label_order: list[int] = [mapping[label] for label in hand.cards]

    return hand.strength, tuple(label_order)


def sort_hands_of_cards(lines: list[str]) -> list[Hand]:
    """Returns sorted hands of cards.

    Args:
        lines: Lines of strings with info about each hand of cards

    Returns:
        List of sorted hands of cards
    """

    type_strength_mapping: dict[str, int] = {
        "five_of_kind": 6,
        "four_of_kind": 5,
        "full_house": 4,
        "three_of_kind": 3,
        "two_pairs": 2,
        "one_pair": 1,
        "high_card": 0,
    }

    label_order_mapping: dict[str, int] = {label: i for i, label in enumerate(reversed("AKQJT98765432"))}

    hands: list[Hand] = []

    for line in lines:
        cards: str = line.split()[0]
        bid: int = int(line.split()[1])
        hands.append(
            Hand(
                cards=cards,
                bid=bid,
                strength=get_strength_of_hand(
                    cards=cards,
                    mapping=type_strength_mapping,
                ),
            )
        )

    return sorted(
        hands,
        key=lambda hand: sort_by_strength_and_labels(
            hand=hand,
            mapping=label_order_mapping,
        ),
    )


def main() -> None:
    """Prints the solution to Day 7, Part One."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    hands: list[Hand] = sort_hands_of_cards(lines=lines)

    print(sum([hands[i].bid * (i + 1) for i in range(len(hands))]))


if __name__ == "__main__":
    main()
