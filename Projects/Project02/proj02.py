quarters = 10
dimes = 10
nickels = 10
pennies = 10

while True:
    print()
    print("\nWelcome to change-making program.")
    print("\nStock: {} quarters, {} dimes, {} nickles, and {} pennies".format(
        quarters, dimes, nickels, pennies))

    price = input(u"Enter the purchase price (xx.xx) or 'q' to quit: ")
    payment = input(u"Enter the payment received in (xx.xx) format or 'q' to quit: ")

    price = int(float(price)*100)
    payment = int(float(payment)*100)

    if price < 0:
        print("The value you entered is negative, please enter a valid value.")
        price = int(float(input("Enter the purchase price (xx.xx) or 'q' to quit: "))*100)

    if payment < 0:
        print("The value you entered is negative, please enter a valid value.")
        payment = int(float(input("Enter the payment amount (xx.xx) or 'q' to quit: "))*100)

    change = payment - price

    quartersBack = change // 25
    change = change % 25
    quarters = quarters - quartersBack
    if quartersBack > quarters:
        print("\nThere is not enough stock to make the change provided. Sorry")
        break

    dimesBack = change // 10
    change = change % 10
    dimes = dimes - dimesBack
    if dimesBack > dimes:
        print("\nThere is not enough stock to make the change provided. Sorry")
        break

    nickelsBack = change // 5
    change = change % 5
    nickels = nickels - nickelsBack
    if nickelsBack > nickels:
        print("\nThere is not enough stock to make the change provided. Sorry")
        break

    penniesBack = change // 1
    change = change % 1
    pennies = pennies - penniesBack
    if penniesBack > pennies:
        print("\nThere is not enough stock to make the change provided. Sorry")
        break

    print("The change back is:", quartersBack, "quarters", dimesBack, "dimes", nickelsBack, "nickels and", penniesBack,
          "pennies.")