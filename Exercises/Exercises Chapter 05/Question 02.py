#CH 5 Q2


# count_case function definition goes here
def count_case(user_input):
    lower = 0
    upper = 0
    for i,ch in enumerate(user_input):
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
    return (upper,lower)

print("-"*30)
print("Count Upper Case and Lower Case")
print("-"*30)

user_input = input("Enter a string (no punctuation): ")
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)