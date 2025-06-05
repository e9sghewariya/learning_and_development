# pylint: disable=line-too-long
# pylint: disable=missing-module-docstring

# # Problem 6

# The sum of the squares of the first ten natural numbers is,

# ```
# 1^2 + 2^2 + ... + 10^2 = 385
# ```

# The square of the sum of the first ten natural numbers is,

# ```
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# ```

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is `3025 − 385 = 2640`.

# ## Part A

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# ```
# answer()
# ```

# ## Part B

# Find the difference between the sum of the squares of the consecutive natural numbers starting with  and p and ending at q and the square of the sum of consecutive natural numbers starting with p and q.

# ```
# solver(p, q)


def answer():
    n = 100
    sum_of_squares = 0

    for i in range(1, n + 1):
        sum_of_squares = sum_of_squares + (i**2)

    square_of_sum = (n * (n + 1) // 2) ** 2
    return square_of_sum - sum_of_squares


print(answer())
# o/p : 25164150

# part b:


def solver(p, q):
    if p > q:
        p, q = q, p  # Ensure p is less than or equal to q

    sum_of_squares = 0
    sum_of_numbers = 0

    for i in range(p, q + 1):
        sum_of_squares += i**2
        sum_of_numbers += i

    square_of_sum = sum_of_numbers**2
    return square_of_sum - sum_of_squares


print(solver(4, 304))
# o/p: 2139282250
