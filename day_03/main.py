def read_file(filename: str) -> list[str]:
    """Reads a text file in the current directory and returns it as a list of strings.

    Args:
        filename: Name of the text file to be read

    Returns:
        Text file represented as a list of strings
    """

    with open(file=filename, mode="r") as file:
        return file.readlines()


def main() -> None:
    """"""

    field: list[str] = read_file(filename="puzzle_input.txt")


if __name__ == "__main__":
    main()
