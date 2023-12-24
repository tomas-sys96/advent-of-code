from dataclasses import dataclass
from collections import defaultdict

FILE_PATH: str = "../puzzle_input.txt"


@dataclass
class Hand:
    cards: str
    bid: int
    strength: int


def get_strength_of_hand(cards: str) -> int:
    """"""

    # TODO: Add type_strength_mapping dict?

    label_count: defaultdict = defaultdict(int)

    for label in cards:
        label_count[label] += 1

    match len(label_count):
        case 1:
            # Five of a kind
            return 7
        case 2:
            if any([count == 4 for count in label_count.values()]):
                # Four of a kind
                return 6
            else:
                # Full house
                return 5
        case 3:
            if any([count == 3 for count in label_count.values()]):
                # Three of a kind
                return 4
            else:
                # Two pairs
                return 3
        case 4:
            # One pair
            return 2
        case _:
            return 1


def sort_by_strength_and_labels(hand: Hand) -> tuple[int, tuple]:
    """"""

    label_order_mapping: dict[str, int] = {label: i for i, label in enumerate(reversed("AKQJT98765432"))}
    label_order: list[int] = [label_order_mapping[label] for label in hand.cards]
    return hand.strength, tuple(label_order)


def sort_hands_of_cards(lines: list[str]) -> list[Hand]:
    """"""

    hands: list[Hand] = []

    for line in lines:
        cards: str = line.split()[0]
        bid: int = int(line.split()[1])
        hands.append(
            Hand(
                cards=cards,
                bid=bid,
                strength=get_strength_of_hand(cards=cards),
            )
        )

    return sorted(hands, key=sort_by_strength_and_labels)


def main() -> None:
    """Prints the solution to Day 7, Part One."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    hands: list[Hand] = sort_hands_of_cards(lines=lines)

    print(sum([hands[i].bid * (i + 1) for i in range(len(hands))]))


if __name__ == "__main__":
    main()
