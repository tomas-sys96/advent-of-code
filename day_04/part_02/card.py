class Card:
    """Definition of a scratchcard.

    Attributes:
        number: Card number
        winning_numbers: Winning numbers
        owned_numbers: Numbers that a person owns
        points: Total points for the card
    """

    def __init__(self, number: int, winning_numbers: list[int], owned_numbers: list[int]) -> None:
        self.number: int = number
        self.winning_numbers: list[int] = winning_numbers
        self.owned_numbers: list[int] = owned_numbers
        self.points: int = 0

    def get_points_for_card(self) -> None:
        """Calculates the sum of points for the card."""

        for number in self.owned_numbers:
            if number in self.winning_numbers:
                self.points += 1

    def get_next_card_numbers(self) -> list[int]:
        """Returns a list of the next card numbers based on the current card number and points.

        Returns:
            List of the next card numbers
        """

        self.get_points_for_card()
        return list(range(self.number + 1, self.number + self.points + 1))
