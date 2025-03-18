def library_sort(arr):
    """
    Implement the Library Sort algorithm (Insertion Sort with binary search).
    
    Library Sort is an adaptive sorting algorithm that uses binary search 
    to reduce the number of comparisons and shifts during insertion.
    
    Args:
        arr (list): The input list to be sorted in ascending order.
    
    Returns:
        list: A new sorted list with elements in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains uncomparable elements.
    """
    # Handle edge cases
    if arr is None:
        raise TypeError("Input cannot be None")
    
    # Create a copy to avoid modifying the original list
    result = []
    
    for item in arr:
        # Find the insertion point using binary search
        if not result:
            result.append(item)
            continue
        
        # Binary search to find the correct insertion point
        left, right = 0, len(result)
        while left < right:
            mid = (left + right) // 2
            if result[mid] < item:
                left = mid + 1
            else:
                right = mid
        
        # Insert the item at the correct position
        result.insert(left, item)
    
    return result