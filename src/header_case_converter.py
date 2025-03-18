def convert_to_header_case(input_string: str) -> str:
    """
    Convert a given string to header case.

    Header case capitalizes the first letter of each word, 
    removing any non-alphanumeric characters and replacing them with spaces.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string converted to header case.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> convert_to_header_case("hello world")
        'Hello World'
        >>> convert_to_header_case("hello-world_test")
        'Hello World Test'
        >>> convert_to_header_case("hello_WORLD-test")
        'Hello World Test'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace non-alphanumeric characters with spaces
    cleaned_chars = []
    for i, char in enumerate(input_string):
        if char.isalpha():
            cleaned_chars.append(char)
        elif char.isdigit():
            # Add space before/after specific numbered sections
            if (i > 0 and input_string[i-1].isalpha() and 
                (i == len(input_string) - 1 or input_string[i+1].isalpha())):
                cleaned_chars.append(' ' + char)
            elif (i < len(input_string) - 1 and input_string[i+1].isalpha() and 
                  (i == 0 or input_string[i-1].isalpha())):
                cleaned_chars.append(char + ' ')
            else:
                cleaned_chars.append(char)
        else:
            cleaned_chars.append(' ')
    
    # Convert to string and split
    cleaned_string = ''.join(cleaned_chars)
    
    # Split the string, convert to title case, and join
    return ' '.join(word.capitalize() for word in cleaned_string.split())