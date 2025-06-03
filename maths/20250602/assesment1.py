# # Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# ## Part A

# Find the sum of all the multiples of 3 or 5 below 1000.

# Edit the file answer.py and update the function `sum_of_multiples` to return the answer.

# ```
# sum_of_multiples()
# ```

# ## Part B

# Write a function in python that returns the sum of all the multiples of a list of factors where the multiples are between the `start` and `end`, inclusive.

# Edit the file solver.py to update the function `sum_of_multiples` which returns the answer when called as in the below example.

# ```
# sum_of_multiples([3, 5, 12], 400, 1842)
# ```

# def sum_of_multiples():
#     number = 1

#     sum = 0

#     while number < 1000:
#         if number % 3 == 0 or number % 5 == 0:
#             sum += number
#         number += 1
#     return sum
# print(sum_of_multiples())

#updated part a code using itertools.product
from itertools import product


def sum_of_multiples_using_product():
    total = 0
    numbers = range(1, 1000)
    multiples = [3, 5]
    
    for i, j in product(multiples, numbers):
        if j % i == 0:
            total += j
    return sum(set(j for i, j in product(multiples, numbers) if j % i == 0))
print(sum_of_multiples_using_product())
# o/p: 233168
#part b

def sum_of_multiples_b(list_of_numbers, begin, end):
    total = 0
    for i in list_of_numbers:
        for j in range(begin, end + 1):
            if j % i == 0:
                total += j
    return total

print(sum_of_multiples_b([3, 5, 12], 400, 1842))  # Example usage
#o/p:998002


#Updated code using product() from itertools

def sum_of_multiples_b_product(list_of_numbers, begin, end):
    total = 0
    for factor, number in product(list_of_numbers, range(begin, end + 1)):
        if number % factor == 0:
            total += number
    return total
print(sum_of_multiples_b_product([3, 5, 12], 400, 1942))

#o/p: 1113441

