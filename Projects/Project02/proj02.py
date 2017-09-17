##############################################################
#  Project 2
#
#   Initialize variables
#
#   Print Welcome message and stock
#   prompt for price and payment outside of loop
#       Check if input is not ideal
#       Cast to int if input is not string
#   Mainloop while not q
#       if price or payment is not q
#        set changeback to 0 for all coins
#           if payment >= price
#               Check if input is non-negative and not string
#               while loops to increment and degrement stock and changeback for each coin
#               print stock and changeback
#
##############################################################


# starting stock
quarters = 10
dimes = 10
nickels = 10
pennies = 10
quartersBack = 0
dimesBack = 0
nickelsBack = 0
penniesBack = 0

print("\nWelcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))

price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

if price == 'q':
    quit()
else:
    price = int(float(price)* 100)

#check for negative price
if price < 0:
    print("Error: purchase price must be non-negative.")
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))
    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

    #check if userinput is quit
    if price == 'q':
        quit()
    else:
        price = int(float(price) * 100)

#cast the input if its not a string
if type(price) != str:
    int(float(price)) * 100

#prompt for payment
payment = input("Input dollars paid (int): ")

#quit if input is q
if payment == "q":
    quit()
else:
    payment = int(float(payment)* 100)

#catch if payment is negative
if payment < 0:
    print("Error: purchase price must be non-negative.")
    payment = input("Input dollars paid (int): ")

    #quit if input is q
    if payment == "q":
        quit()
    else:
        payment = int(float(payment) * 100)

#cast to number if its not a string
if type(payment) != str:
    int(float(payment)) * 100

#mainloop
while price != 'q' or payment != 'q':


    if price != 'q' and payment != 'q':

        #set change back to 0
        quartersBack = 0
        dimesBack = 0
        nickelsBack = 0
        penniesBack = 0

        #continue only if payment is greater than price
        if payment >= price:

            # Check for negative values
            if price < 0:
                print("Error: purchase price must be non-negative.")
                print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
                    quarters, dimes, nickels, pennies))
                price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

                if type(price) != str:
                    int(float(price)) * 100
                else:
                    break

            #check if payment is negative
            if payment < 0:
                print("Error: purchase price must be non-negative.")
                payment = input("Input dollars paid (int): ")

                if type(payment) != str:
                    int(float(payment)) * 100
                else:
                    break

            # calculate change
            change = payment - price

            # calculate exact change back with a while loop
            while quarters > 0 and change >= 25:
                change = change - 25
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

            # print stock
            if payment == price:
                print("No change.")
            elif payment > price:
                print("Collect change below: ")

            #print the change back only if there is any for each coin
            if quartersBack > 0:
                print("Quarters: " + str(quartersBack))
            if dimesBack > 0:
                print("Dimes: " + str(dimesBack))
            if nickelsBack > 0:
                print("Nickels: " + str(nickelsBack))
            if penniesBack > 0:
                print("Pennies: " + str(penniesBack))

            #print stock
            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
                quarters, dimes, nickels, pennies))

            # input price and payment amount
            price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

            #quit if its q
            if price == 'q':
                quit()
            else:
                price = int(float(price) * 100)

            #prompt for payment
            payment = input("Input dollars paid (int): ")

            #quit if q
            if payment == "q":
                quit()
            else:
                payment = int(float(payment) * 100)

        #if the payment < price
        else:
            print("Error: insufficient payment.")
            payment = int(float(input("Input dollars paid (int): ")) * 100)