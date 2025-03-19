def reverse_substring_vowels(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels in a specified substring of a given string.
    
    Args:
        s (str): The input string
        start (int): The starting index of the substring (inclusive)
        end (int): The ending index of the substring (exclusive)
    
    Returns:
        str: A new string with vowels in the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are invalid
        TypeError: If input is not a string or indices are not integers
    """
    # Validate input types
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers")
    
    # Validate indices
    if start < 0 or end > len(s) or start > end:
        raise ValueError("Invalid substring indices")
    
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Extract vowels from the substring
    substring_vowels = [char for char in chars[start:end] if char in vowels]
    
    # If no vowels, return original string
    if not substring_vowels:
        return s
    
    # Reverse the vowels
    vowel_index = len(substring_vowels) - 1
    
    # Create a new list to modify
    result = chars.copy()
    
    # Replace vowels in the substring
    for i in range(start, end):
        if chars[i] in vowels:
            result[i] = substring_vowels[vowel_index]
            vowel_index -= 1
    
    return ''.join(result)