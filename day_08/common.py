from typing import Callable


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


def is_target_node(node: str, target_node: str) -> bool:
    """Checks if a node is the target node.

    Args:
        node: Node to be checked
        target_node: Target node

    Returns:
        True if the node is the target node, False otherwise
    """

    return node == target_node


def endswith_target_character(node: str, target_node: str) -> bool:
    """Checks if a node string ends with the target character.

    Args:
        node: Node to be checked
        target_node: Target node

    Returns:
        True if the node string ends with the target character, False otherwise
    """

    return node.endswith(target_node[-1])


def get_steps_to_target_node(
    instructions: str,
    nodes: dict[str, tuple],
    current_node: str,
    target_node: str,
) -> int:
    """Calculates the number of steps it takes to reach a target node based on the instructions.

    Args:
        instructions: Instructions to follow
        nodes: Dictionary of node-elements pairs
        current_node: Starting node
        target_node: Target node

    Returns:
        Number of steps
    """

    is_target: Callable[[str, str], bool] = (
        endswith_target_character if target_node.startswith("??") else is_target_node
    )

    steps: int = 0
    while True:
        instruction: str = instructions[steps % len(instructions)]
        steps += 1

        element_index: int = 0 if instruction == "L" else 1
        current_node: str = nodes[current_node][element_index]

        if is_target(current_node, target_node):
            return steps
