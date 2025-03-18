def bubble_sort(arr):
    """
    Implement the bubble sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Create a copy of the input list to avoid modifying the original
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy of the list to sort
    sorted_arr = arr.copy()
    
    # Bubble sort algorithm
    n = len(sorted_arr)
    for i in range(n):
        # Flag to optimize by breaking early if no swaps occur
        swapped = False
        
        # Last i elements are already in place, so reduce the range
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            try:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap the elements
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swapped = True
            except TypeError:
                raise TypeError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return sorted_arr