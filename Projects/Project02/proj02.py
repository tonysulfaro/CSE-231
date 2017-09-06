quarters = 10
dimes = 10
nickels = 10
pennies = 10

while True:
    print()
    print("\nWelcome to change-making program.")
    print("\nStock: {} quarters, {} dimes, {} nickles, and {} pennies".format(
        quarters, dimes, nickels, pennies))

    price = int(float(input("Enter the purchase price (xx.xx) or 'q' to quit: "))*100)
    payment = int(float(input("Enter the payment received in (xx.xx) format or 'q' to quit: "))*100)

    if price < 0:
        print("The value you entered is negative, please enter a valid value.")
        price = int(float(input("Enter the purchase price (xx.xx) or 'q' to quit: "))*100)

    if payment < 0:
        print("The value you entered is negative, please enter a valid value.")
        payment = int(float(input("Enter the payment amount (xx.xx) or 'q' to quit: "))*100)

    # if user enters 'q', halt the program
    if price == 'q' or payment == 'q':
        break

    change = payment - price
    print(change)
    quartersBack = change // quarters
    temp = change - quartersBack * quarters
    dimesBack = temp // dimes
    tempd = temp - dimesBack * dimes
    nickelsBack = temp // nickels
    tempn = tempd - nickelsBack * nickels
    penniesBack = tempn // pennies
    tempp = tempn - penniesBack * pennies

    print("The change back is:", quartersBack, "quarters", dimesBack, "dimes", nickelsBack, "nickels and", penniesBack,
          "pennies.")