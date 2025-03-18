"""
Implementation of the LZ78 compression algorithm.

The LZ78 compression algorithm works by building a dictionary of previously seen 
sequences and replacing repeated sequences with references to the dictionary.
"""

def lz78_compress(input_string):
    """
    Compress the input string using the LZ78 compression algorithm.
    
    Args:
        input_string (str): The string to be compressed.
    
    Returns:
        list: A list of tuples representing the compressed data.
              Each tuple is (index, character), where:
              - index is the reference to a previous sequence (0 if new)
              - character is the next character
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary and compressed output
    dictionary = {0: ''}  # 0 index represents empty string
    current_index = 1
    compressed = []
    
    # Current sequence being processed
    current_sequence = ''
    
    # Compress the input string
    for char in input_string:
        # Try to find the longest match in the dictionary
        test_sequence = current_sequence + char
        
        # If the sequence is in the dictionary
        match_found = False
        for dict_index, dict_value in dictionary.items():
            if dict_value == test_sequence:
                current_sequence = test_sequence
                match_found = True
                break
        
        # If no match found, add to compressed output and update dictionary
        if not match_found:
            # Find the index of the longest prefix
            prefix_index = 0
            for dict_index, dict_value in dictionary.items():
                if dict_value == current_sequence:
                    prefix_index = dict_index
                    break
            
            # Add to compressed output
            compressed.append((prefix_index, char))
            
            # Add new sequence to dictionary
            dictionary[current_index] = test_sequence
            current_index += 1
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle any remaining sequence
    if current_sequence:
        for dict_index, dict_value in dictionary.items():
            if dict_value == current_sequence:
                compressed.append((dict_index, ''))
                break
    
    return compressed

def lz78_decompress(compressed_data):
    """
    Decompress the LZ78 compressed data.
    
    Args:
        compressed_data (list): A list of tuples from LZ78 compression
    
    Returns:
        str: The decompressed original string
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If input contains invalid compression data
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    # Initialize dictionary and output
    dictionary = {0: ''}
    current_index = 1
    output = []
    
    # Decompress the data
    for index, char in compressed_data:
        # Validate input
        if not isinstance(index, int) or index < 0:
            raise ValueError(f"Invalid dictionary index: {index}")
        
        # Retrieve the referenced sequence
        if index not in dictionary:
            raise ValueError(f"Dictionary index {index} not found")
        
        # Construct the current sequence
        current_sequence = dictionary[index] + char
        output.append(current_sequence)
        
        # Add to dictionary
        dictionary[current_index] = current_sequence
        current_index += 1
    
    # Join and return the decompressed string
    return ''.join(output)