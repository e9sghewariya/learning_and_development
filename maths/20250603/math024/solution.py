"""solution.py - Solution for Project Euler problem 24.
This script contains the solution to the problem of
finding the millionth lexicographic permutation of digits 0-9,
and a generalized function to find the nth lexicographic permutation of any sequence.
"""

import math


def get_kth_permutation(seq, k):
    """Helper function to Find the k-th lexicographic permutation of a sequence."""
    seq = sorted(seq)
    k -= 1
    result = []

    while seq:
        n = len(seq)
        fact = math.factorial(n - 1)
        index = k // fact
        result.append(seq.pop(index))
        k %= fact

    return "".join(result)


def answer():
    """Find the millionth lexicographic permutation of digits 0-9."""
    digits = list("0123456789")
    k = 1000000
    return get_kth_permutation(digits, k)


def solver(seq="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", n=1):
    """Find the nth lexicographic permutation of a given sequence."""
    seq_list = list(seq)
    return get_kth_permutation(seq_list, n)
