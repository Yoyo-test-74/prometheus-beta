from typing import Dict, List, Tuple

def shannon_fano_encode(data: str) -> Tuple[Dict[str, str], str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str): Input string to be encoded
    
    Returns:
        Tuple containing:
        - Dictionary of character to binary code mapping
        - Encoded binary string
    
    Raises:
        ValueError: If input is empty
    """
    # Check for empty input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Special case for single character
    if len(set(data)) == 1:
        return {data[0]: '0'}, '0' * len(data)
    
    # Calculate character frequencies
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Generate Shannon-Fano codes
    def generate_codes(chars: List[Tuple[str, int]], prefix: str = '') -> Dict[str, str]:
        # Base case: single character
        if len(chars) <= 1:
            return {chars[0][0]: prefix} if chars else {}
        
        # Divide the list into two roughly equal groups
        total = sum(count for _, count in chars)
        current_sum = 0
        split_index = 0
        
        for i, (_, count) in enumerate(chars):
            current_sum += count
            if current_sum >= total / 2:
                split_index = i
                break
        
        # Recursively generate codes for both groups
        left_group = chars[:split_index + 1]
        right_group = chars[split_index + 1:]
        
        codes = {}
        codes.update(generate_codes(left_group, prefix + '0'))
        codes.update(generate_codes(right_group, prefix + '1'))
        
        return codes
    
    # Generate codes
    code_map = generate_codes(sorted_chars)
    
    # Encode the input string
    encoded = ''.join(code_map[char] for char in data)
    
    return code_map, encoded

def shannon_fano_decode(code_map: Dict[str, str], encoded: str) -> str:
    """
    Decode a Shannon-Fano encoded string.
    
    Args:
        code_map (Dict[str, str]): Mapping of characters to their binary codes
        encoded (str): Encoded binary string
    
    Returns:
        str: Decoded original string
    
    Raises:
        ValueError: If encoded string cannot be decoded
    """
    # Special case for single character encoding
    if len(code_map) == 1:
        char = list(code_map.keys())[0]
        return char * (len(encoded) // len(code_map[char]))
    
    # Create reverse mapping
    reverse_map = {code: char for char, code in code_map.items()}
    
    # Decode the string
    decoded = []
    current_code = ''
    
    for bit in encoded:
        current_code += bit
        if current_code in reverse_map:
            decoded.append(reverse_map[current_code])
            current_code = ''
    
    # Check if entire string was decoded
    if current_code:
        raise ValueError("Could not decode entire input string")
    
    return ''.join(decoded)