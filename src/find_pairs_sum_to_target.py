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
    
    # Use a dictionary to track number indices
    num_indices = {}
    pairs = set()
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        # If complement exists in previous indices
        if complement in num_indices:
            # Check all previous indices of the complement
            for j in num_indices[complement]:
                # Ensure we're not using the same index
                # and ensure order to avoid duplicates
                if j < i:
                    pair = tuple(sorted((complement, num)))
                    pairs.add(pair)
        
        # Track indices for each number
        if num not in num_indices:
            num_indices[num] = []
        num_indices[num].append(i)
    
    # Convert set of pairs to sorted list
    return sorted(list(pairs))