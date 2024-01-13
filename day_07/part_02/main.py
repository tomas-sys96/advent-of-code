from collections import defaultdict

from day_07.hands import Hand, HandRankGrader

FILE: str = "../puzzle_input.txt"


class HandRankGraderP2(HandRankGrader):
    @staticmethod
    def get_strength_of_hand(cards: str, mapping: dict[str, int]) -> int:
        label_count: defaultdict = defaultdict(int)
        for label in cards:
            label_count[label] += 1

        jokers: int = label_count.get("J", 0)

        match len(label_count):
            case 1:
                return mapping["five_of_kind"]

            case 2:
                if jokers:
                    return mapping["five_of_kind"]
                if any([count == 4 for count in label_count.values()]):
                    return mapping["four_of_kind"]
                return mapping["full_house"]

            case 3:
                if any([count == 3 for count in label_count.values()]):
                    if jokers in [1, 3]:
                        return mapping["four_of_kind"]
                    return mapping["three_of_kind"]
                if jokers == 2:
                    return mapping["four_of_kind"]
                if jokers == 1:
                    return mapping["full_house"]
                return mapping["two_pairs"]

            case 4:
                if jokers in [1, 2]:
                    return mapping["three_of_kind"]
                return mapping["one_pair"]

            case _:
                if jokers:
                    return mapping["one_pair"]
                return mapping["high_card"]


def main() -> None:
    """Prints the solution to Day 7, Part Two."""

    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.readlines()

    grader: HandRankGraderP2 = HandRankGraderP2(label_order="J23456789TQKA")
    hands: list[Hand] = grader.sort_hands_of_cards(lines=lines)

    print(sum([hands[i].bid * (i + 1) for i in range(len(hands))]))


if __name__ == "__main__":
    main()
