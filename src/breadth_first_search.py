from collections import deque
from typing import Dict, List, Optional, Any

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search (BFS) on a graph.

    Args:
        graph (Dict[Any, List[Any]]): A dictionary representing the graph, 
                                      where keys are nodes and values are lists of adjacent nodes.
        start (Any): The starting node for the BFS traversal.

    Returns:
        List[Any]: A list of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid dictionary or contains invalid adjacency lists.
    """
    # Validate input graph
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")

    # Validate start node
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")

    # Validate graph structure
    for node, adjacents in graph.items():
        if not isinstance(adjacents, list):
            raise TypeError(f"Adjacency list for node {node} must be a list")

    # Initialize BFS
    visited = []
    queue = deque([start])
    visited_set = set([start])

    # Perform BFS
    while queue:
        current = queue.popleft()
        visited.append(current)

        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in visited_set:
                queue.append(neighbor)
                visited_set.add(neighbor)

    return visited