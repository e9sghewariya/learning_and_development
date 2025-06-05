""" "
assessment014.py
This script contains solutions to the Project Euler Problem No. 14,
which involves finding the starting number under one million that
produces the longest Collatz sequence.
It also includes a function to find the number with the longest Collatz sequence within a
specified range defined by parameters `p` and `q`.
"""

# <!-- # Problem No. 14

# ## Longest Collatz Sequence

# The following iterative sequence is defined for the set of positive integers:

# $n \to n/2$ ($n$ is even)

# $n \to 3n + 1$ ($n$ is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# ```math
# 13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.
# ```

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet
# (Collatz Problem), it is thought that all starting numbers finish at 1.

# ## Part A

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# Edit the file answer.py and update the function `answer()` to return the answer.

# ## Part B

# Write a function in python that returns
# - `None` if neither p nor q are defined
# - the number which returns the longest collatz
# sequence such that the number is between (a) 1 and `p`
# if only `p` is defined and (b) `p` and `q` if both `p` and `q` are defined

# ```python
# solver(p: int = None, q: int = None)
# ```

# ## References


# [Project Euler Problem 14](https://projecteuler.net/problem=14)
# (https://en.wikipedia.org/wiki/Collatz_conjecture)
# (https://www.quantamagazine.org/why-mathematicians-still-cant-solve-
# the-collatz-conjecture-20200922/) -->
def answer():
    """
    Find the starting number under one million that produces the longest Collatz sequence.
    """
    max_length = 0
    starting_number = 0

    for i in range(1, 1000001):

        n = i
        length = 1

        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            length += 1
        if length > max_length:
            max_length = length
            starting_number = i

    return starting_number


print(answer())

# o/p: 837799


def solver(p: int = None, q: int = None):
    """This is the generic function to find
    the number with the longest Collatz sequence
    within a specified range defined by parameters p and q."""
    if p is None and q is None:
        return None

    if p is not None and q is None:
        start, end = 1, p
    elif p is not None and q is not None:
        start, end = p, q
    else:
        return None

    max_length = 0
    number_with_max_length = start

    for i in range(start, end + 1):
        n = i
        length = 1
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            length += 1

        if length > max_length:
            max_length = length
            number_with_max_length = i

    return number_with_max_length


print(solver())
print(solver(10000))  # Example with only p defined
print(solver(10000, 20000))  # Example with both p and q defined
# o/p: 837799
# if p and q are defined: o/p : None
# if p is 10000 , q is undefined : o/p : 6171
# if p is 10000 and q is 20000 : o/p : 17647
