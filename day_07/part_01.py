from collections import defaultdict

from day_07.common import Hand, HandRankGrader

FILE: str = "puzzle_input.txt"


class HandRankGraderP1(HandRankGrader):
    @staticmethod
    def get_strength_of_hand(cards: str, mapping: dict[str, int]) -> int:
        label_count: defaultdict = defaultdict(int)
        for label in cards:
            label_count[label] += 1

        match len(label_count):
            case 1:
                return mapping["five_of_kind"]
            case 2:
                if any([count == 4 for count in label_count.values()]):
                    return mapping["four_of_kind"]
                return mapping["full_house"]
            case 3:
                if any([count == 3 for count in label_count.values()]):
                    return mapping["three_of_kind"]
                return mapping["two_pairs"]
            case 4:
                return mapping["one_pair"]
            case _:
                return mapping["high_card"]


def main() -> None:
    """Prints the solution to Day 7, Part One."""

    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.readlines()

    grader: HandRankGraderP1 = HandRankGraderP1(label_order="23456789TJQKA")
    hands: list[Hand] = grader.sort_hands_of_cards(lines=lines)

    print(sum([hands[i].bid * (i + 1) for i in range(len(hands))]))


if __name__ == "__main__":
    main()
