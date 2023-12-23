def separate_numbers(numbers: str) -> tuple[list[str], list[str]]:
    """Separates the winning and owned numbers.

    Args:
        numbers: All card numbers

    Returns:
        tuple:
            winning_numbers: Winning numbers,
            owned_numbers: Numbers that a person owns
    """

    winning_numbers: list[str] = [number.strip() for number in numbers.split("|")[0].split()]
    owned_numbers: list[str] = [number.strip() for number in numbers.split("|")[1].split()]

    return winning_numbers, owned_numbers
