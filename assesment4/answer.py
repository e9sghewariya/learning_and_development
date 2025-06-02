
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

#part b

def answer_b(n, p, q):

    num_of_digits = num_of_digits(n)

    max_palindrome = 0
    for i in range():
        for j in range():
            product = i * j
            if check_palindrome(product) and product > max_palindrome:
                max_palindrome = product

def number_of_digits(num):
    return len(str(num))

    return max_p
