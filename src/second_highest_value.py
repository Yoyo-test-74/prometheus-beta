def find_second_highest(sorted_nums):
    """
    Find the second highest value in a sorted list of integers.

    Args:
        sorted_nums (list): A sorted list of integers in ascending or descending order.

    Returns:
        int or None: The second highest value in the list, or None if the list 
                     does not contain at least two unique values.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty.
    """
    # Check for valid input
    if not isinstance(sorted_nums, list):
        raise TypeError("Input must be a list of integers")
    
    if len(sorted_nums) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Remove duplicates while preserving order
    unique_nums = list(dict.fromkeys(sorted_nums))
    
    # Check if there are at least two unique values
    if len(unique_nums) < 2:
        return None
    
    # Determine if the list is in ascending or descending order
    if sorted_nums[0] < sorted_nums[-1]:
        # Ascending order
        return unique_nums[-2]
    else:
        # Descending order
        return unique_nums[1]