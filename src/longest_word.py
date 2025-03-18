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
    
    # Remove leading/trailing whitespace
    stripped_sentence = sentence.strip()
    
    # Check for empty string
    if not stripped_sentence:
        raise ValueError("Input sentence contains no valid words")
    
    # Use regex to split words, removing punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', sentence)
    
    # If no words after splitting, raise ValueError
    if not words:
        raise ValueError("Input sentence contains no valid words")
    
    # Find the first longest word (stable sort by length)
    return sorted(words, key=len, reverse=True)[0]