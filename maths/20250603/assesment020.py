""""
assessment020: Factorial Digit Sum
"""
# # Problem No. 20

# ## Factorial Digit Sum

# $n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.

# For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,
# and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.

# ## Part A

# Find the sum of the digits in the number $100!$.

# Edit the file answer.py and update the function `answer()` to return the answer.

# ## Part B

# Generalize the solution in Part A to find the sum of the digits in any number $n!$.

# Update the function `solver()` in `solver.py` with your generalized solution.

# ```python
# solver(n: int)
# ```

def get_factorial(n):
    """Calculate the factorial of a number n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def answer():
    """Find the sum of the digits in the number 100!."""
    fact_of_100 = get_factorial(100)
    return sum(int(digit) for digit in str(fact_of_100))
print(answer())
#o/p:648
def solver(n):
    """Find the sum of the digits in the number n!."""
    fact_of_n = get_factorial(n)
    return sum(int(digit) for digit in str(fact_of_n))
print(solver(1000))  # Example usage
#o/p: 10539
