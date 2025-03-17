def count_words(text: str) -> int:
    """
    Count the number of words in a given string.

    Args:
        text (str): The input string to count words in.

    Returns:
        int: The number of words in the string.

    Notes:
        - Words are defined as sequences of non-whitespace characters
        - Multiple consecutive whitespace characters are treated as a single separator
        - Empty string or string with only whitespace returns 0
    """
    # If text is None or empty, return 0
    if not text:
        return 0
    
    # Strip leading and trailing whitespace and split on whitespace
    words = text.strip().split()
    
    # Return the number of words
    return len(words)