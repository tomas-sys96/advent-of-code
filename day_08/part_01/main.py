FILE_PATH: str = "../puzzle_input.txt"


def get_nodes(lines: list[str]) -> dict[str, tuple]:
    """Returns a dictionary of nodes and their elements.

    Args:
        lines: Lines of strings with info about nodes and elements

    Returns:
        Dictionary of node-elements pairs
    """

    nodes: dict[str, tuple] = {}
    for line in lines:
        node: str = line.split(" = ")[0]
        elements: tuple = tuple(line.split(" = ")[1].removeprefix("(").removesuffix(")\n").split(", "))
        nodes[node] = elements

    return nodes


def get_steps_to_target_node(instructions: str, nodes: dict[str, tuple], target_node: str) -> int:
    """Calculates the number of steps it takes to reach a target node based on the instructions.

    Args:
        instructions: Instructions to follow
        nodes: Dictionary of node-elements pairs
        target_node: Node to be reached

    Returns:
        Number of steps
    """

    node: str = "AAA"
    steps: int = 0
    while True:
        instruction: str = instructions[steps % len(instructions)]
        steps += 1

        match instruction:
            case "L":
                node = nodes[node][0]
            case _:
                node = nodes[node][1]

        if node == target_node:
            return steps


def main() -> None:
    """Prints the solution to Day 8, Part One."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    instructions: str = lines[0].removesuffix("\n")
    nodes: dict[str, tuple] = get_nodes(lines=lines[2:])

    print(
        get_steps_to_target_node(
            instructions=instructions,
            nodes=nodes,
            target_node="ZZZ",
        )
    )


if __name__ == "__main__":
    main()
