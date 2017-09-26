#range_test function definition goes here
def range_test(num):
    if num < 1 or num > 500:
        return False
    else:
        return True

num = int(input("Enter a number: "))
if range_test(num):
    print( "{:d} is in range.".format(num))
else:
    print("The number you entered is outside the range!")