def search_sorted_matrix(matrix, target):
    """
    Search for a target value in a 2D matrix with sorted inner lists.
    
    Args:
        matrix (List[List[int]]): A 2D matrix where inner lists are sorted in ascending order
        target (int): The value to search for in the matrix
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Time Complexity: O(m * log(n)), where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If matrix is empty or contains non-integer elements
    """
    # Input validation
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list of lists")
    
    if not matrix:
        return False
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    # Check if matrix is empty or contains empty rows
    if not matrix[0]:
        return False
    
    # Validate matrix elements are integers
    try:
        for row in matrix:
            if not all(isinstance(x, int) for x in row):
                raise ValueError("Matrix must contain only integers")
    except TypeError:
        raise ValueError("Matrix must contain only integers")
    
    # Efficient search using binary search on each row
    for row in matrix:
        # Binary search within each row
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False