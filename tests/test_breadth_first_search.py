import pytest
from src.breadth_first_search import breadth_first_search

def test_basic_bfs():
    """Test BFS on a simple connected graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = breadth_first_search(graph, 'A')
    assert result[0] == 'A'
    assert set(result) == set(graph.keys())

def test_single_node_graph():
    """Test BFS on a graph with a single node."""
    graph = {'A': []}
    result = breadth_first_search(graph, 'A')
    assert result == ['A']

def test_disconnected_graph():
    """Test BFS on a graph with disconnected nodes."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result_a = breadth_first_search(graph, 'A')
    result_c = breadth_first_search(graph, 'C')
    assert set(result_a) == {'A', 'B'}
    assert set(result_c) == {'C', 'D'}

def test_invalid_start_node():
    """Test BFS with a start node not in the graph."""
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        breadth_first_search(graph, 'X')

def test_invalid_graph_type():
    """Test BFS with an invalid graph type."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search([], 'A')

def test_invalid_adjacency_list():
    """Test BFS with an invalid adjacency list."""
    graph = {'A': 'not a list'}
    with pytest.raises(TypeError, match="Adjacency list for node A must be a list"):
        breadth_first_search(graph, 'A')

def test_cyclic_graph():
    """Test BFS on a graph with cycles."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    result = breadth_first_search(graph, 'A')
    assert result[0] == 'A'
    assert set(result) == set(graph.keys())

def test_nodes_with_multiple_adjacencies():
    """Test BFS on a graph with nodes having multiple adjacencies."""
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E'],
        'C': ['A', 'F'],
        'D': ['A', 'G'],
        'E': ['B'],
        'F': ['C'],
        'G': ['D']
    }
    result = breadth_first_search(graph, 'A')
    assert result[0] == 'A'
    assert set(result) == set(graph.keys())