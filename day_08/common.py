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
