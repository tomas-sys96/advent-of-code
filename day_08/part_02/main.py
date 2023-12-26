FILE_PATH: str = "../test_input.txt"


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


def get_steps_to_target_nodes(instructions: str, nodes: dict[str, tuple], target_character: str) -> int:
    """Calculates the number of steps it takes to reach all target nodes at once based on the instructions.

    Args:
        instructions: Instructions to follow
        nodes: Dictionary of node-elements pairs
        target_character: Character that all the target nodes should end with

    Returns:
        Number of steps
    """

    current_nodes: list[str]
    next_nodes: list[str] = [node for node in nodes.keys() if node.endswith("A")]

    steps: int = 0
    while True:
        instruction: str = instructions[steps % len(instructions)]
        steps += 1

        element_index: int = 0 if instruction == "L" else 1

        current_nodes = next_nodes.copy()
        next_nodes.clear()
        matches: int = 0

        for node in current_nodes:
            next_node: str = nodes[node][element_index]
            next_nodes.append(next_node)

            if next_node.endswith(target_character):
                matches += 1

        if matches == len(current_nodes):
            return steps


def main() -> None:
    """Prints the solution to Day 8, Part Two."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    instructions: str = lines[0].removesuffix("\n")
    nodes: dict[str, tuple] = get_nodes(lines=lines[2:])

    print(
        get_steps_to_target_nodes(
            instructions=instructions,
            nodes=nodes,
            target_character="Z",
        )
    )


if __name__ == "__main__":
    main()
