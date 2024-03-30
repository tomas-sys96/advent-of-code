from common import get_nodes, get_steps_to_target_node

FILE: str = "puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 8, Part One."""

    with open(file=FILE, mode="r") as file:
        lines: list[str] = file.readlines()

    instructions: str = lines[0].removesuffix("\n")
    nodes: dict[str, tuple] = get_nodes(lines=lines[2:])

    print(
        get_steps_to_target_node(
            instructions=instructions,
            nodes=nodes,
            current_node="AAA",
            target_node="ZZZ",
        )
    )


if __name__ == "__main__":
    main()
