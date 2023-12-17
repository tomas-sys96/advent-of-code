FILE_PATH: str = "../puzzle_input.txt"


def separate_numbers(numbers: str) -> tuple[list[int], list[int]]:
    """"""

    winning_numbers: list[int] = [int(number.strip()) for number in numbers.split("|")[0].split()]
    owned_numbers: list[int] = [int(number.strip()) for number in numbers.split("|")[1].split()]

    return winning_numbers, owned_numbers


def get_points_from_card(winning_numbers: list[int], owned_numbers: list[int]) -> int:
    """"""

    points: int = 0
    for number in owned_numbers:
        if number in winning_numbers:
            if points:
                points *= 2
            else:
                points += 1

    return points


def main() -> None:
    """"""

    scratchcard_points: int = 0

    with open(file=FILE_PATH, mode="r") as file:
        while True:
            line: str = file.readline()
            if not line:
                break

            winning_numbers: list[int]
            owned_numbers: list[int]
            winning_numbers, owned_numbers = separate_numbers(numbers=line.split(":")[1])

            scratchcard_points += get_points_from_card(winning_numbers=winning_numbers, owned_numbers=owned_numbers)

    print(scratchcard_points)


if __name__ == "__main__":
    main()
