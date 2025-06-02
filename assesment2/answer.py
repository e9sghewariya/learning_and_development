def answer():
    sum = 0

    num1 = 0
    num2 = 1

    number = num1 + num2

    while number <= 4000000:
        if number % 2 == 0:
            sum += number

        num1 = num2
        num2 = number
        number = num1 + num2
    return sum

print(answer())
