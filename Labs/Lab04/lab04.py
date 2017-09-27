#Lab 04

#Part A: Leap Year
year = int(input("input a year: "))

def leap_year(year):

    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(leap_year(year))

#Part B: Rotate
s = input("Input a String: ")
n = int(input("Input an Int: "))
def rotate(s,n):
    return s[-n:]+s[:-n]
print(rotate(s,n))

#Part C: Digit Count
numInput = int(float(input("Enter in an Int or Float: ")))
numInput = str(numInput)
evens = '2468'
odds = '13579'

def digit_count(numInput):

    evenCount = 0
    oddCount = 0
    zeroCount = 0

    for i,num in enumerate(numInput):
        if numInput != '0':
            if num in evens:
                evenCount += 1
            elif num in odds:
                oddCount += 1
            else:
                zeroCount += 1

    return (evenCount,oddCount,zeroCount)
print(digit_count(numInput))

#Part D: Float Check
userString = input("Enter a String to see if it's a Digit: ")

def float_check(userString):
    return userString.isdigit()
print(float_check(userString))

