#part a
def sum_of_multiples():

    number = 1
    sum = 0

    while number <= 1000:
        if (num%3 == 0 or num%5 == 0):
            sum += number
        number += 1
    return sum

#part b
def sum_of_multiples_2(list_of_numbers, begin, end):

    sum = 0

    while i in list_of_numbers:

        for j in range(begin, end + 1):
            if j % i == 0:
                sum += j
    return sum
