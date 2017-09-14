# Project 2

# starting stock
quarters = 10
dimes = 10
nickels = 10
pennies = 10
ChangeString = ""

print("\nWelcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))

price = input(u"Enter the purchase price (xx.xx) or 'q' to quit: ")
if type(price) is int:
    price = int(price)*100
else:
    quit()

payment = input(u"Input dollars paid (int): ")
if type(payment) is int:
    payment = int(payment)*100
else:
    quit()

while price != 'q' or payment != 'q':

    if price != 'q' and payment != 'q':

        # convert price and payment to raw cent amount
        price = int(float(price) * 100)
        payment = int(float(payment) * 100)

        # Check for negative values
        if price < 0:
            print("The value you entered is negative, please enter a valid value.")
            price = int(float(input("Enter the purchase price (xx.xx) or 'q' to quit: ")) * 100)

        if payment < 0:
            print("The value you entered is negative, please enter a valid value.")
            payment = int(float(input("Input dollars paid (int): ")) * 100)

        # calculate change
        change = payment - price

        # calculate exact change back
        quartersBack = change // 25
        change = change % 25
        quarters = quarters - quartersBack

        dimesBack = change // 10
        change = change % 10
        dimes = dimes - dimesBack

        nickelsBack = change // 5
        change = change % 5
        nickels = nickels - nickelsBack

        penniesBack = change // 1
        change = change % 1
        pennies = pennies - penniesBack

        # idk where this is supposed to go yet
        #print("\nThere is not enough stock to make the change provided. Sorry")


        if quartersBack > 0:
            ChangeString += "Quarters: " + str(quartersBack)
        if dimesBack > 0:
            ChangeString += "Dimes: " + str(dimesBack)
        if nickelsBack > 0:
            ChangeString += "Nickels: " + str(nickelsBack)
        if penniesBack > 0:
            ChangeString += "Pennies: " + str(penniesBack)

        # print stock
        if payment == price:
            print("No change.")
        else:
            print("Collect change below: ")

        print(ChangeString)

        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    #input price and payment amount
    price = input(u"Enter the purchase price (xx.xx) or 'q' to quit: ")
    if type(price) is int:
        price = int(price)*100
    else:
        break
    payment = input(u"Input dollars paid (int): ")
    if type(payment) is int:
        payment = int(payment)*100
    else:
        break
