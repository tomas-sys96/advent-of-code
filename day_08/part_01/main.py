from day_08.common import get_nodes

FILE_PATH: str = "../puzzle_input.txt"


def get_steps_to_target_node(instructions: str, nodes: dict[str, tuple], current_node: str, target_node: str) -> int:
    """Calculates the number of steps it takes to reach a target node based on the instructions.

    Args:
        instructions: Instructions to follow
        nodes: Dictionary of node-elements pairs
        current_node: Starting node
        target_node: Node to be reached

    Returns:
        Number of steps
    """

    steps: int = 0
    while True:
        instruction: str = instructions[steps % len(instructions)]
        steps += 1

        element_index: int = 0 if instruction == "L" else 1
        current_node: str = nodes[current_node][element_index]

        if current_node == target_node:
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
            current_node="AAA",
            target_node="ZZZ",
        )
    )


if __name__ == "__main__":
    main()
