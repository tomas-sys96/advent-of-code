from typing import Optional


def read_file(filename: str) -> list[str]:
    """Reads a text file in the current directory and returns its contents as a list of strings.

    Args:
        filename: Name of the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=filename, mode="r") as file:
        return [line.replace("\n", "") for line in file.readlines()]


def main() -> None:
    """"""

    field: list[str] = read_file(filename="puzzle_input.txt")

    digits: list[str] = []
    number: Optional[int] = None

    for line in field:
        for character_index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
            elif not line[character_index + 1].isdigit() and digits:
                number = int("".join(digits))
                digits = []

            if number:
                print("some logic")
                number = None


if __name__ == "__main__":
    main()
