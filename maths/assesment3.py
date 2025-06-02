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

def check_prime(num):
    if(num <= 1):
        return False
    
    count = 0

    for i in range(1, num):
        if(num % i == 0):
            count += 1

    if(count == 2):
        return True
    else:
        return False
    

def answer():
    max = 0

    for i in range(1, 600851475143):
        if(check_prime(i)):
            max = i
    return max
print(answer())



def answer(value):

    num = 1
    max = 0
    while num > value:

        if (value % num == 0) and check_prime(num):
            if num > max:
                max = num

        num += 1
    return max

print(answer(475143))  