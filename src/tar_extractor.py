import os
import tarfile
from typing import Union, List, Optional

def extract_tar_archive(
    tar_path: str, 
    extract_path: Optional[str] = None, 
    specific_files: Optional[Union[str, List[str]]] = None
) -> List[str]:
    """
    Extract files from a tar archive with flexible options.

    Args:
        tar_path (str): Path to the tar archive file
        extract_path (Optional[str]): Directory to extract files to. 
            If None, extracts to the same directory as the tar file.
        specific_files (Optional[Union[str, List[str]]]): 
            Single file or list of files to extract. If None, extracts all files.

    Returns:
        List[str]: Paths of extracted files

    Raises:
        FileNotFoundError: If tar file does not exist
        ValueError: If tar path is invalid or extraction fails
        tarfile.TarError: For tar-specific errors
    """
    # Validate input
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar archive not found: {tar_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(tar_path) or '.'

    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)

    # Convert single file to list if needed
    if isinstance(specific_files, str):
        specific_files = [specific_files]

    # Extracted files list
    extracted_files = []

    try:
        # Open tar archive
        with tarfile.open(tar_path, 'r:*') as tar:
            # If no specific files specified, extract all
            if specific_files is None:
                tar.extractall(path=extract_path)
                extracted_files = [
                    os.path.join(extract_path, member.name) 
                    for member in tar.getmembers() 
                    if member.isfile()
                ]
            else:
                # Validate and extract specific files
                for file in specific_files:
                    # Check if file exists in archive
                    try:
                        tar.getmember(file)
                    except KeyError:
                        raise ValueError(f"File {file} not found in archive")

                    # Extract specific files
                    tar.extract(file, path=extract_path)
                    extracted_files.append(os.path.join(extract_path, file))

    except tarfile.TarError as e:
        raise ValueError(f"Error extracting tar archive: {e}")

    return extracted_files