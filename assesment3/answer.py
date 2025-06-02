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

    for i in range(1, 600,851,475,143):
        if(check_prime(i)):
            max = i
    return max
