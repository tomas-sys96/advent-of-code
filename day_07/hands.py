from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Hand:
    cards: str
    bid: int
    strength: int


class HandRankGrader(ABC):
    def __init__(self, label_order: str) -> None:
        self.label_order: str = label_order

    @staticmethod
    @abstractmethod
    def get_strength_of_hand(cards: str, mapping: dict[str, int]) -> int:
        """Returns the strength of a hand based on its type.

        Args:
            cards: String of card labels
            mapping: Type to strength mapping

        Returns:
            Strength value
        """

        pass

    @staticmethod
    def sort_by_strength_and_labels(hand: Hand, mapping: dict[str, int]) -> tuple[int, tuple]:
        """Sorts hands of cards based on their strength, then based on the order of individual labels.

        Args:
            hand: Hand of cards
            mapping: Label to order mapping

        Returns:
            tuple:
                Hand strength -- first rule,
                Numbered labels -- second rule
        """

        numbered_labels: list[int] = [mapping[label] for label in hand.cards]

        return hand.strength, tuple(numbered_labels)

    def sort_hands_of_cards(self, lines: list[str]) -> list[Hand]:
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

        label_order_mapping: dict[str, int] = {label: i for i, label in enumerate(self.label_order)}

        hands: list[Hand] = []

        for line in lines:
            cards: str = line.split()[0]
            bid: int = int(line.split()[1])
            hands.append(
                Hand(
                    cards=cards,
                    bid=bid,
                    strength=self.get_strength_of_hand(
                        cards=cards,
                        mapping=type_strength_mapping,
                    ),
                )
            )

        return sorted(
            hands,
            key=lambda hand: self.sort_by_strength_and_labels(
                hand=hand,
                mapping=label_order_mapping,
            ),
        )
