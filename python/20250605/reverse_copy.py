"""This module provides a function to copy the contents of a file"""

def reverse_copy(source, destination):
    """
    Copies the contents of the source file 
    to the destination file in reverse order.
    """
    with open(source, 'r',encoding='utf-8') as src:
        lines = src.readlines()

    with open(destination, 'w', encoding='utf-8') as dest:
        dest.writelines(reversed(lines))
