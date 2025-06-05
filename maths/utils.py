""" Utility functions for mathematical operations.""" 
# utils.py
import math

def check_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
