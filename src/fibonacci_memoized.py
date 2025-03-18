def fibonacci_memoized(n: int, memo: dict = None) -> int:
    """
    Calculate the nth Fibonacci number using recursion with memoization.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (0-based index).
        memo (dict, optional): Memoization dictionary to store previously calculated values.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> fibonacci_memoized(0)
        0
        >>> fibonacci_memoized(1)
        1
        >>> fibonacci_memoized(5)
        5
    """
    # Initialize memoization dictionary if not provided
    if memo is None:
        memo = {}
    
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Check if value is already memoized
    if n in memo:
        return memo[n]
    
    # Recursive calculation with memoization
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    
    return memo[n]