"""This module counts occurrences of a target word in a large-size file."""
import zipfile

def count_word_in_file_or_zip(file_path, target_word, chunk_size=1024):
    """
    Counts occurrences of a target word in 
    a text file or the first file in a zip archive.
    """
    target_word = target_word.lower()
    count = 0

    if zipfile.is_zipfile(file_path):
        # Handle zip file
        with zipfile.ZipFile(file_path) as z:
            file_names = z.namelist()
            if not file_names:
                return 0  # Empty zip archive

            # Use the first file inside the zip
            with z.open(file_names[0]) as f:
                while chunk := f.read(chunk_size):
                    text = chunk.decode('utf-8', errors='ignore').lower()
                    count += text.count(target_word)
    else:
        # Handle regular text file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            while chunk := f.read(chunk_size):
                count += chunk.lower().count(target_word)

    return count
