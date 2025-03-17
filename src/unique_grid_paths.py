def count_unique_paths(m: int, n: int) -> int:
    """
    Count the number of unique paths from top-left to bottom-right in an m x n grid.
    
    Only allowed movements are moving right or down.
    Uses dynamic programming with optimized compute.
    
    Args:
        m (int): Number of rows in the grid
        n (int): Number of columns in the grid
    
    Returns:
        int: Number of unique paths from top-left to bottom-right
    
    Raises:
        ValueError: If m or n is less than 1
    
    Examples:
        >>> count_unique_paths(3, 7)
        28
        >>> count_unique_paths(3, 2)
        3
    """
    # Input validation
    if m < 1 or n < 1:
        raise ValueError("Grid dimensions must be at least 1x1")
    
    # Optimized approach for combinatorics
    # Total unique paths is (m+n-2) choose (m-1)
    # Uses math and factorials instead of dynamic programming
    def factorial(x):
        if x <= 1:
            return 1
        return x * factorial(x - 1)
    
    def combination(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))
    
    return combination(m + n - 2, m - 1)