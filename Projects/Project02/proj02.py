# Project 2

# starting stock
quarters = 10
dimes = 10
nickels = 10
pennies = 10
quartersBack = 0
dimesBack = 0
nickelsBack = 0
penniesBack = 0
ChangeString = ""

print("\nWelcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))

price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

if price == 'q':
    quit()
else:
    price = int(float(price)* 100)


payment = input("Input dollars paid (int): ")

if payment == "q":
    quit()
else:
    payment = int(float(payment)* 100)

if payment < price:
    print("Error: insufficient payment.")

while price != 'q' or payment != 'q':

    if price != 'q' and payment != 'q':
        quartersBack = 0
        dimesBack = 0
        nickelsBack = 0
        penniesBack = 0


        # Check for negative values
        if price < 0:
            print("The value you entered is negative, please enter a valid value.")
            price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

            if type(price) != str:
                int(float(price)) * 100
            else:
                break

        if payment < 0:
            print("The value you entered is negative, please enter a valid value.")
            payment = input("Input dollars paid (int): ")

            if type(payment) != str:
                int(float(payment)) * 100
            else:
                break

        # calculate change
        change = payment - price

        # calculate exact change back maybe use a while loop??

        while quarters > 0 and change >= 25:
            change = change -25
            quartersBack += 1
            quarters -= 1

        while dimes > 0 and change >= 10:
            change -= 10
            dimesBack += 1
            dimes -= 1

        while nickels > 0 and change >= 5:
            change -= 5
            nickelsBack += 1
            nickels -= 1

        while pennies > 0 and change >= 1:
            change -= 1
            penniesBack += 1
            pennies -= 1

        if change > 0:
            print("\nError: ran out of coins.")
            break


        if quartersBack > 0:
            ChangeString += "Quarters: " + str(quartersBack)
        if dimesBack > 0:
            ChangeString += " Dimes: " + str(dimesBack)
        if nickelsBack > 0:
            ChangeString += " Nickels: " + str(nickelsBack)
        if penniesBack > 0:
            ChangeString += " Pennies: " + str(penniesBack)

        # print stock
        if payment == price:
            print("No change.")
        else:
            print("Collect change below: ")

        print(ChangeString)
        changeString = ""

        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

    #input price and payment amount

    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

    if price == 'q':
        quit()
    else:
        price = int(float(price) * 100)

    payment = input("Input dollars paid (int): ")

    if payment == "q":
        quit()
    else:
        payment = int(float(payment) * 100)

    if payment < price:
        print("Error: insufficient payment.")
