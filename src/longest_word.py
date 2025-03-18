import re

def find_longest_word(sentence):
    """
    Find the first longest word in a given sentence based on the ordering in the original sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The first longest word in the sentence based on its original order.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains only whitespace.
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Split the sentence into words, keeping the original order
    orig_words = re.findall(r'\b[a-zA-Zà-ÿÀ-Ÿ]+\b', sentence)
    
    # If no words after splitting, raise specific error
    if not orig_words:
        raise ValueError("Input sentence contains no valid words")
    
    # Find the first longest word of maximum length
    max_length = len(max(orig_words, key=len))
    
    # Return the first word with max length 
    for word in orig_words:
        if len(word) == max_length:
            return word