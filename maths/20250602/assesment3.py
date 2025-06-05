"""This module is for prime numbers and factors."""

# # Problem 3

# The prime factors of 13,195 are 5, 7, 13, and 29.

# ## Part A

# What is the largest prime factor of the number 600,851,475,143?

# Edit the file answer.py and update the function `answer()` to return the answer.

# ```
# answer()
# ```

# ## Part B

# Write a function in python that returns the largest prime factor of a given number.

# Edit the file solver.py to update the function `solver` to
# return the answer when called as in the below example.

# ```
# solver(value)
# ```

# updated check prime function
import math


def answer():
    """
    Returns the largest prime factor of 600851475143.
    """
    n = 600851475143
    factor = 2
    last_factor = 1
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            last_factor = factor
        else:
            factor += 1 if factor == 2 else 2
    if n > 1:
        return n
    return last_factor


print(answer())


def answer_2(value):
    """Return the largest prime factor of the given number."""
    if value <= 1:
        return None
    while value % 2 == 0:
        last_factor = 2
        value //= 2
    factor = 3
    max_factor = math.isqrt(value)
    while factor <= max_factor and value > 1:
        while value % factor == 0:
            last_factor = factor
            value //= factor
            max_factor = math.isqrt(value)
        factor += 2
    return value if value > 1 else last_factor


print(answer_2(10))
