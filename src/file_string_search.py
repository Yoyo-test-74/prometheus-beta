def search_string_in_file(file_path, search_string):
    """
    Search for a specific string in a file.

    Args:
        file_path (str): Path to the file to be searched.
        search_string (str): The string to search for in the file.

    Returns:
        list: A list of line numbers (1-indexed) where the string is found.
        If the string is not found, returns an empty list.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        TypeError: If file_path or search_string is not a string.
        ValueError: If search_string is empty.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(search_string, str):
        raise TypeError("search_string must be a string")
    
    # Check for empty search string
    if not search_string:
        raise ValueError("search_string cannot be empty")
    
    # Initialize results list
    line_matches = []
    
    try:
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            # Enumerate lines to get line numbers
            for line_num, line in enumerate(file, 1):
                # Case-sensitive check for full word
                if search_string in line.strip():
                    line_matches.append(line_num)
        
        return line_matches
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")