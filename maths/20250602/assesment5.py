"""Smallest number divisible by all numbers in a range"""

# # Problem 5

# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# ## Part A

# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

# Edit the file answer.py and update the function `answer()` to return
# the answer.

# ```
# answer()
# ```

# ## Part B

# Write a function in python
# that returns
# the smallest positive number that is evenly
# divisible by all of the
# numbers between the range `p` and `q`
# , inclusive.

# Use the range from the lesser of `p` and `q`
# to the greater of `p` and `q`. Make no assumption
# about which is lesser or greater.

# Edit the file solver.py to update the function
# `solver` to return the answer when called as in
# the below example.

# ```
# solver(p, q)
# ```

# def answer():

#     num = 2

#     while True:

#         divisible = True

#         for i in range(1, 21):
#             if num % i != 0:
#                 divisible = False
#                 break

#         if divisible:
#             return num
#         num += 1
# print(answer())

# updated code :
import math


def lcm(a, b):
    """Return the Least Common Multiple of two integers a and b."""
    return abs(a * b) // math.gcd(a, b)


def answer():
    """
    Returns the smallest positive number that is evenly divisible by all numbers from 1 to 20.

    This uses the Least Common Multiple (LCM) approach to ensure minimal computation.
    """
    num = 1
    for i in range(2, 21):  # from 2 to 20
        num = lcm(num, i)
    return num


print(answer())  # Output: 232792560


# def solver(p, q):
#     if p > q:
#         p, q = q, p

#     num = 2

#     while True:

#         divisible = True

#         for i in range(p, q + 1):
#             if num % i != 0:
#                 divisible = False
#                 break


#         if divisible:
#             return num
#         num += 1
# updated code:
def solver(p, q):
    """
    Returns the smallest positive number evenly divisible by
    all numbers in the inclusive range between p and q.

    Args:
        p (int): One end of the range.
        q (int): The other end of the range.

    Returns:
        int: The least common multiple of all integers
        between min(p, q) and max(p, q).
    """
    if p > q:
        p, q = q, p
    num = 1
    for i in range(p, q + 1):
        num = lcm(num, i)
    return num


print(solver(1, 20))
