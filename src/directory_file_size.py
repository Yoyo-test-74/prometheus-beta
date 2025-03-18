import os

def calculate_directory_total_size(directory_path):
    """
    Calculate the total size of all files in a given directory.

    Args:
        directory_path (str): Path to the directory to calculate total file size.

    Returns:
        int: Total size of all files in bytes.

    Raises:
        TypeError: If directory_path is not a string.
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Validate input type
    if not isinstance(directory_path, str):
        raise TypeError("Directory path must be a string")

    # Normalize and expand the directory path
    directory_path = os.path.abspath(os.path.expanduser(directory_path))

    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    # Check if path is a directory
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")

    total_size = 0

    # Walk through directory and calculate total file size
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Use lstat to handle symlinks without following them
                total_size += os.path.getsize(file_path)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to access directory: {directory_path}")

    return total_size