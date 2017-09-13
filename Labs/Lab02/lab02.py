#constants
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

n_str = input("Input an integer (0 terminates): ")
userInput = int(n_str)
#main loop
while userInput != 0:

    #evaluate input and increment counters
    if userInput > 0:

        positive_int_count += 1

        if userInput%2 == 0:
            even_sum += userInput
            even_count += 1

        else:
            odd_sum += userInput
            odd_count += 1

    else:
        print("You entered a negative number. It will not be recorded.")

        # user input
    n_str = input("Input an integer (0 terminates): ")
    userInput = int(n_str)

#print counts of values
print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)