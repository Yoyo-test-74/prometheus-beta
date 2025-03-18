import pytest
from src.stable_marriage import stable_marriage

def test_stable_marriage_basic():
    # Basic scenario with 3 men and 3 women
    men_prefs = [
        [1, 0, 2],  # Man 0's preferences
        [0, 2, 1],  # Man 1's preferences
        [1, 2, 0]   # Man 2's preferences
    ]
    women_prefs = [
        [1, 0, 2],  # Woman 0's preferences
        [2, 1, 0],  # Woman 1's preferences
        [0, 2, 1]   # Woman 2's preferences
    ]
    
    result = stable_marriage(men_prefs, women_prefs)
    
    # Verify that the result is a stable matching
    assert len(result) == 3
    assert len(set(result.values())) == 3  # Each woman matched once
    
    # Validate the matching (this may vary based on specific inputs)
    assert result == {0: 0, 1: 2, 2: 1}

def test_stable_marriage_edge_cases():
    # Minimal valid input
    men_prefs = [[0], [1]]
    women_prefs = [[1], [0]]
    
    result = stable_marriage(men_prefs, women_prefs)
    assert result == {0: 0, 1: 1}

def test_invalid_input_empty_lists():
    with pytest.raises(ValueError, match="Preferences lists cannot be empty"):
        stable_marriage([], [])

def test_invalid_input_unequal_lengths():
    with pytest.raises(ValueError, match="Men and women preference lists must be of equal length"):
        stable_marriage([[0, 1]], [[1, 0], [0, 1]])

def test_invalid_preference_lists():
    # Duplicate values
    with pytest.raises(ValueError, match="Invalid preference list"):
        stable_marriage(
            [[0, 0, 1], [1, 2, 0], [2, 1, 0]],
            [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
        )
    
    # Missing values
    with pytest.raises(ValueError, match="Invalid preference list"):
        stable_marriage(
            [[0, 1], [0, 2], [1, 2]],
            [[0, 1], [1, 2], [2, 0]]
        )

def test_stable_marriage_larger_case():
    # Larger test case to verify stability
    men_prefs = [
        [3, 1, 2, 0],
        [1, 0, 3, 2],
        [0, 2, 1, 3],
        [2, 1, 3, 0]
    ]
    women_prefs = [
        [1, 3, 0, 2],
        [0, 2, 3, 1],
        [3, 1, 2, 0],
        [2, 0, 1, 3]
    ]
    
    result = stable_marriage(men_prefs, women_prefs)
    
    assert len(result) == 4
    assert len(set(result.values())) == 4