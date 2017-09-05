number = int(input("Input an int: "))
temp = 0

for x in range(number):
    temp += 1
    if number%temp == 0:
        print(temp)