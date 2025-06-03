# # Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# ## Part A

# What is the 10,001st prime number?

# ```
# answer()
# ```

# ## Part B

# Write a function, `solver()` to find the nth prime number?

# ```
# solver(n)
# ```
import math

def check_prime(num):
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

def answer():
    count = 0
    num = 1
    while count < 10001:
        num += 1
        if check_prime(num):
            count += 1
    return num
print(answer())
#output: 104743


#part b:

def solver(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if check_prime(num):
            count += 1
    return num
print(solver(11005)) 
#o/p: 116507
