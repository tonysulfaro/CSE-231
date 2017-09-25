# is_prime function definition goes here
def is_prime(num):
    n = 1
    factorCount = 0
    for x in range(num):
        if num%n == 0:
            factorCount += 1
        n += 1
    if factorCount > 2:
        return False
    elif factorCount <= 2:
        return True
num = int(input("Input an integer greater than 1: "))

if is_prime(num):
    print("{:d} is a prime".format(num))
else:
    print("{:d} is not a prime".format(num))