def count_unique_paths(m: int, n: int) -> int:
    """
    Count the number of unique paths from top-left to bottom-right in an m x n grid.
    
    Only allowed movements are moving right or down.
    
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
    
    # Create a 2D grid to store unique path counts
    dp = [[1] * n for _ in range(m)]
    
    # Calculate unique paths using dynamic programming
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]