import re

def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first one encountered.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains only whitespace.
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Use regex to split words, supporting Unicode characters
    words = re.findall(r'\b[a-zA-Zà-ÿÀ-Ÿ]+\b', sentence)
    
    # If no words after splitting, raise specific error
    if not words:
        raise ValueError("Input sentence contains no valid words")
    
    # Find the first longest word using stable sorting
    return sorted(words, key=len, reverse=True)[0]