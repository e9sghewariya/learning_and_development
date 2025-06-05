"""This module contains functions to find prime numbers."""
# Problem 7

# By listing the first six prime
# numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.

# ## Part A

# What is the 10,001st prime number?

# ```
# answer()
# ```

# ## Part B

# Write a function, `solver()` to find
# the nth prime number?

# ```
# solver(n)
# ```
from utils import check_prime

def answer():
    """
    Find the 10,001st prime number.

    Returns:
        int: The 10,001st prime number.
    """

    count = 0
    num = 1
    while count < 10001:
        num += 1
        if check_prime(num):
            count += 1
    return num


print(answer())
# output: 104743


# part b:


def solver(n):
    """
    Find the nth prime number.

    Args:
        n (int): The position of the prime number to find.

    Returns:
        int: The nth prime number.
    """

    count = 0
    num = 1
    while count < n:
        num += 1
        if check_prime(num):
            count += 1
    return num


print(solver(11005))
# o/p: 116507
