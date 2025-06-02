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

# Write a function in python that returns the smallest positive number that is evenly divisible by all of the numbers between the range `p` and `q`, inclusive.

# Use the range from the lesser of `p` and `q` to the greater of `p` and `q`. Make no assumption about which is lesser or greater.

# Edit the file solver.py to update the function `solver` to return the answer when called as in the below example.

# ```
# solver(p, q)
# ```

def answer():
    
    num = 2
    
    while True:
        
        divisible = True
        
        for i in range(1, 21):
            if num % i != 0:
                divisible = False
                break
        
        if divisible:
            return num  
        num += 1
print(answer())

def solver(p, q):
    if p > q:
        p, q = q, p  
    
    num = 2
    
    while True:
        
        divisible = True
        
        for i in range(p, q + 1):
            if num % i != 0:
                divisible = False
                break
        
        if divisible:
            return num 
        num += 1
        
print(solver(1, 20))