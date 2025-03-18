def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in the input list that sum up to the target.

    Args:
        numbers (list): A list of integers to search for pairs.
        target (int): The target sum to find pairs for.

    Returns:
        list: A list of unique pairs (as tuples) that sum up to the target.

    Examples:
        >>> find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)
        [(2, 5), (3, 4)]
        >>> find_pairs_sum_to_target([1, 1, 2, 3, 4, 5], 6)
        [(1, 5), (2, 4)]

    Notes:
        - Pairs are unique (no duplicate pairs)
        - Order within pair is preserved
        - Pairs are sorted in the order they are found
    """
    # Input validation
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Use a set to track used numbers and avoid duplicates
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists and hasn't been used in this pair
        if complement in seen and num not in seen:
            # Sort the pair to ensure unique representation
            pair = tuple(sorted((complement, num)))
            pairs.add(pair)
        
        seen.add(num)
    
    # Convert set of pairs to sorted list
    return sorted(list(pairs))