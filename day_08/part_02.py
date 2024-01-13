from math import lcm

from day_08.common import get_nodes, get_steps_to_target_node

FILE: str = "puzzle_input.txt"


def main() -> None:
    """Prints the solution to Day 8, Part Two."""

    with open(file=FILE, mode="r") as file:
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
                target_node="??Z",
            )
        )

    # Print the least common multiple of all steps
    print(lcm(*steps))


if __name__ == "__main__":
    main()
