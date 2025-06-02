def answer_b(star, end, even=False, odd=False):
    if not even and not odd:
        return 0

    sum = 0
    for i in range(star, end + 1):
        if (even and i % 2 == 0) or (odd and i % 2 != 0):
            sum += i
    return sum
