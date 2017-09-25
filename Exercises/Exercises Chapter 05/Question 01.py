# find_min function definition goes here
def find_min(first,second):
    if first < second:
        return first
    elif second < first:
        return second
    else:
        return ("The Numbers are the Same Value")

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = find_min(first, second)
print("Minimum: ", minimum)