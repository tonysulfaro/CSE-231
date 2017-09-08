# starting stock
quarters = 10
dimes = 10
nickels = 10
pennies = 10
ChangeString = ""

print("\nWelcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickles, and {} pennies".format(
        quarters, dimes, nickels, pennies))
while True:

    #input price and payment amount
    price = input(u"Enter the purchase price (xx.xx) or 'q' to quit: ")
    if price.__contains__("q"):
        break
    payment = input(u"Input dollars paid (int):")
    if payment.__contains__("q"):
        break

    #convert price and payment to raw cent amount
    price = int(float(price) * 100)
    payment = int(float(payment) * 100)

    #Check for negative values
    if price < 0:
        print("The value you entered is negative, please enter a valid value.")
        price = int(float(input("Enter the purchase price (xx.xx) or 'q' to quit:")) * 100)

    if payment < 0:
        print("The value you entered is negative, please enter a valid value.")
        payment = int(float(input("Input dollars paid (int):")) * 100)

    #calculate change
    change = payment - price

    #calculate exact change back
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

    if quartersBack > 0:
        ChangeString += str(quarters) + " quarters"
    if dimesBack > 0:
        ChangeString += str(dimesBack) + " dimes"
    if nickelsBack > 0:
        ChangeString += str(nickelsBack) + " nickels"
    if penniesBack > 0:
        ChangeString += str(penniesBack) + " pennies"

    #print stock
    print("Collect change below:\n", ChangeString)#, quartersBack, "Quarters", dimesBack, "dimes", nickelsBack, "nickles and", penniesBack,
          #"pennies.")

    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))