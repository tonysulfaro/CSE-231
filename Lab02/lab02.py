n_str = input("Input an integer (0 terminates): ")
userInput = int(n_str)
# Good stuff goes here

#constants
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

#counter
while userInput != 0:
    #user input
    n_str = input("Input an integer (0 terminates): ")
    userInput = int(n_str)

    if userInput%2 == 0:
        even_sum += userInput
        even_count += 1
    else:
        odd_sum += userInput
        odd_count += 1






print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
