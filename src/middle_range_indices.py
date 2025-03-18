def find_middle_range_indices(sorted_list, range_size):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers.
        range_size (int): The number of elements to include on each side of the middle.

    Returns:
        list: A list of indices of elements within the specified range of the middle value.

    Raises:
        ValueError: If range_size is negative or the list is empty.
        TypeError: If inputs are not of the correct type.
    """
    # Input validation
    if not isinstance(sorted_list, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(range_size, int):
        raise TypeError("Range size must be an integer")
    
    if range_size < 0:
        raise ValueError("Range size cannot be negative")
    
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    # Determine the middle index
    list_length = len(sorted_list)
    
    # Calculate middle index for both even and odd length lists
    if list_length % 2 == 0:
        # For even length, use the lower of the two middle indices
        middle_index = (list_length // 2) - 1
    else:
        # For odd length, use the exact middle index
        middle_index = list_length // 2
    
    # Calculate start and end indices of the range
    start_index = max(0, middle_index - range_size)
    end_index = min(list_length - 1, middle_index + range_size)
    
    # Return the indices within the range
    return list(range(start_index, end_index + 1))