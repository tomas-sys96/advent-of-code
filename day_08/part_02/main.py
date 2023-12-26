from math import lcm

from day_08.common import get_nodes

FILE_PATH: str = "../puzzle_input.txt"


def get_steps_to_target_node(
    instructions: str,
    nodes: dict[str, tuple],
    current_node: str,
    target_character: str,
) -> int:
    """Calculates the number of steps it takes to reach a target node based on the instructions.

    Args:
        instructions: Instructions to follow
        nodes: Dictionary of node-elements pairs
        current_node: Starting node
        target_character: Character that the target node should end with

    Returns:
        Number of steps
    """

    steps: int = 0
    while True:
        instruction: str = instructions[steps % len(instructions)]
        steps += 1

        element_index: int = 0 if instruction == "L" else 1
        current_node: str = nodes[current_node][element_index]

        if current_node.endswith(target_character):
            return steps


def main() -> None:
    """Prints the solution to Day 8, Part Two."""

    with open(file=FILE_PATH, mode="r") as file:
        lines: list[str] = file.readlines()

    instructions: str = lines[0].removesuffix("\n")
    nodes: dict[str, tuple] = get_nodes(lines=lines[2:])
    starting_nodes: list[str] = [node for node in nodes.keys() if node.endswith("A")]

    # Get the minimum number of steps that it takes to reach the target node for every starting node
    steps: list[int] = []
    for node in starting_nodes:
        steps.append(
            get_steps_to_target_node(
                instructions=instructions,
                nodes=nodes,
                current_node=node,
                target_character="Z",
            )
        )

    # Print the least common multiple of all steps
    print(lcm(*steps))


if __name__ == "__main__":
    main()
