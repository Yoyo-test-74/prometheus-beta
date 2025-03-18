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
    cleaned_string = ''.join(char if char.isalnum() else ' ' for char in input_string)
    
    # Split the string, convert to title case, and join
    return ' '.join(word.capitalize() for word in cleaned_string.split())