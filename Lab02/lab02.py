#constants
userInput = ""
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

#main loop
while userInput != 0:

    #user input
    n_str = input("Input an integer (0 terminates): ")
    userInput = int(n_str)

    #evaluate input and increment counters
    if userInput%2 == 0 and userInput > 0:
        even_sum += userInput
        even_count += 1

    elif userInput%2 != 0 and userInput > 0:
        odd_sum += userInput
        odd_count += 1

    if userInput > 0:
        positive_int_count += 1


#print counts and sums
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)