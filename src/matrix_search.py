def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The integer to search for in the matrix
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Time Complexity: O(m * log(n)), where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If the matrix is empty or contains non-integer elements
    """
    # Validate input
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list of lists")
    
    if not matrix or not matrix[0]:
        return False
    
    # Check matrix structure and validate elements
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Matrix must be a list of lists")
        
        if not all(isinstance(elem, int) for elem in row):
            raise ValueError("Matrix must contain only integer elements")
    
    # Binary search on rows, then binary search on the selected row
    rows, cols = len(matrix), len(matrix[0])
    
    # Binary search for the potential row
    top, bottom = 0, rows - 1
    while top <= bottom:
        mid_row = (top + bottom) // 2
        
        # If target is within this row's range
        if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
            # Binary search within this row
            left, right = 0, cols - 1
            while left <= right:
                mid_col = (left + right) // 2
                
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] < target:
                    left = mid_col + 1
                else:
                    right = mid_col - 1
            
            return False
        
        # Navigate to the correct row
        if target < matrix[mid_row][0]:
            bottom = mid_row - 1
        else:
            top = mid_row + 1
    
    return False