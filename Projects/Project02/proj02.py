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

    quartersBack = change // 25
    change = change % 25

    dimesBack = change // 10
    change = change % 10

    nickelsBack = change // 5
    change = change % 5

    penniesBack = change // 1
    change = change % 1

    print("The change back is:", quartersBack, "quarters", dimesBack, "dimes", nickelsBack, "nickels and", penniesBack,
          "pennies.")