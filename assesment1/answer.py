def sum_of_multiples():
    number = 1

    sum = 0

    while number <= 1000:
        if number % 3 == 0 or number % 5 == 0:
            sum += number
        number += 1
    return sum

#part b

def sum_of_multiples_b(list_of_numbers, begin, end):
    sum = 0

    while i in list_of_numbers:

        for( j = begin to end):
            if(j%i == 0):
                sum += j
    return sum
