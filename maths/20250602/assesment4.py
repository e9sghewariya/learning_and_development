# # Problem 4

# A palindromic number reads the same both ways. The largest 
# palindrome made from the product of two 2-digit numbers is 9009.

# ```
# 9009 = 91 x 99
# ```

# ## Part A

# Find the largest palindrome made from the product of two 3-digit numbers.

# Edit the file answer.py and update the function `answer()` to return the answer.

# ```
# answer()
# ```

# ## Part B

# Write a function that returns the largest palindrome from the product of two n-digit numbers where both numbers are inside a range.

# ```
# solver(n, p=None, q=None)
# ```

# The range is defined as between:
# - the first n digit number to p if only p is provided
# - p and q if p and q are both provided

def check_palindrome(num):
    reverse = 0

    original = num
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse

def answer():
    max_palindrome = 0

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if check_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

print(answer())
#o/p: 906609
#part b

def solver(n, p=None, q=None):
    
    lower = 10**(n - 1)
    upper = 10**n - 1

    # Adjust bounds if p and/or q are provided
    if p is not None and q is not None:
        lower = min(p, q)
        upper =  max(p, q)
    elif p is not None:
        lower = 10**(n - 1) 
        upper = p

    max_palindrome = 0
    for i in range(upper, lower - 1, -1):
        for j in range(i, lower - 1, -1):  
            product = i * j
            if product <= max_palindrome:
                break  
            if check_palindrome(product):
                if product > max_palindrome:
                    max_palindrome = product
    return max_palindrome

print(solver(3, 20, 322))  
#o/p: 94249
