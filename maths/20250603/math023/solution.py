"""
solution.py

This script contains the solution to the problem of
finding the sum of all positive integers that cannot
be expressed as the sum of two abundant numbers.
"""

from itertools import product


def get_divisors(n):
    """Return a list of divisors of n, excluding n itself."""
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def check_abundant(n):
    """Check if a number n is abundant."""
    return sum(get_divisors(n)) > n


def answer():
    """Find the sum of all positive integers
    that cannot be expressed as the sum of two abundant numbers."""
    limit = 28123

    abundant = [i for i in range(12, limit + 1) if check_abundant(i)]

    can_be_written = [False] * (limit + 1)
    for i, a in enumerate(abundant):
        for b in abundant[i:]:
            s = a + b
            if s <= limit:
                can_be_written[s] = True
            else:
                break

    return sum(i for i, x in enumerate(can_be_written) if not x)


print(answer())
# o/p: 4179871


def solver(n, p, q):
    """
    Returns the sum of all positive integers that cannot be expressed as
    the sum of `n` abundant numbers in the range [p, q], using itertools.product.
    """
    if n < 1 or p > q:
        return 0

    abundant = [i for i in range(p, q + 1) if check_abundant(i)]

    if not abundant:
        return 0

    max_sum = n * q

    possible_sums = set(
        sum(comb) for comb in product(abundant, repeat=n) if sum(comb) <= max_sum
    )

    return sum(i for i in range(1, max_sum + 1) if i not in possible_sums)


print(solver(2, 1, 28123))  # Example usage
# o/p: 52862271
