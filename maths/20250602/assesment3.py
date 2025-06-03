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

#updated check prime function
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



def answer(value):
    for num in range(value // 2, 2, -1):
        if num % 2 == 0:
            continue 
        if value % num == 0 and check_prime(num):
            return num  
    return value if check_prime(value) else None

print(answer(475143))  

