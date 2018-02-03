#calculates for gcd testing
from math import gcd

def main():

    number = int(input("input a number "))
    second_number = int(input("input another number "))

    gcd_number = gcd(number, second_number)

    #print("the gcd of ", number, " and ", second_number, " is ", gcd_number)
    print(gcd_number)

if __name__ == "__main__":
    main()