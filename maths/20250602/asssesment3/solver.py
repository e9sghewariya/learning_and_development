def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer(value):

    num = 1;
    max = 0
    while num > value:

        if (value % num == 0) and check_prime(num):
            if num > max:
                max = num

        num += 1
    return max