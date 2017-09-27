userString = input("Enter a String to see if it's a Digit: ")

def float_check(userString):
    decimalCount = 0
    digitcount = 0
    numbers = '1234567890'
    for i, ch in enumerate(userString):

        if ch.isdigit():
            digitcount +=1
        elif ch == '.':
            decimalCount +=1
        else:
            return False

    return decimalCount <= 1

print(float_check(userString))