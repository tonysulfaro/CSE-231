# purchase price and payment will be kept in cents

quarters = 10
dimes = 10
nickels = 10
pennies = 10
change = 0
changequarters = 0
changedimes = 0
changenickels = 0
changepennies = 0

print("\nWelcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
      .format(quarters, dimes, nickels, pennies))

# prompt for price
price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

if price == 'q':
    quit()
else:
    price = int(float(price) * 100)

if (price < 0):

    print("Error: purchase price must be non-negative.")
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
          .format(quarters, dimes, nickels, pennies))
    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

    if price == 'q':
        quit()
    else:
        price = int(float(price) * 100)

# prompt for payment
payment = input("Input dollars paid (int): ")

if payment == 'q':
    quit()
else:
    payment = int(float(payment) * 100)


if (payment < 0):

    print("Error: purchase price must be non-negative.")
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
          .format(quarters, dimes, nickels, pennies))

    payment = input("Input dollars paid (int): ")

    if payment == 'q':
        quit()
    else:
        payment = int(float(payment) * 100)

# check if values are negative



if (payment < 0):
    print("Error: purchase price must be non-negative.")

while (price) != 'q' or payment != 'q':

    change = 0
    changequarters = 0
    changedimes = 0
    changenickels = 0
    changepennies = 0

    if payment >= price:

        change = payment - price
        # insufficient funds?

        if payment == 'q':
            quit()

        if (payment < 0):

            print("Error: purchase price must be non-negative.")
            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies"
                  .format(quarters, dimes, nickels, pennies))
            payment = input("Input dollars paid (int): ")

            if payment == 'q':
                quit()
            else:
                payment = int(float(payment) * 100)

                # Fill in the good stuff here instead of the following print


                # if change > 0:

                # quarters = quarters - (payment - price)//(.25)

                # dimes = dimes - ((payment - price)-(.25*(10-quarters)))//.10

                # nickels = nickels - (((payment - price)-(.25*(10-quarters))-(.10*(10-dimes)))//.05

        # correct

        while change >= 25 and quarters > 0:
            quarters = quarters - 1
            change = change - 25
            changequarters = changequarters + 1

        while change >= 10 and dimes > 0:
            dimes = dimes - 1
            change = change - 10
            changedimes = changedimes + 1

        while change >= 5 and nickels > 0:
            nickels = nickels - 1
            change = change - 5
            changenickels = changenickels + 1

        while change >= 1 and pennies > 0:
            pennies = pennies - 1
            change = change - 1
            changepennies = changepennies + 1

        if change > 0:
            print("\nError: ran out of coins.")
            break

        if payment == price:
            print("No change.")
        elif payment > price:
            print("\nCollect change below: ")

        if changequarters > 0:
            print("Quarters:", changequarters)
        if changedimes > 0:
            print("Dimes:", changedimes)
        if changenickels > 0:
            print("Nickels:", changenickels)
        if changepennies > 0:
            print("Pennies:", changepennies)

        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

        if price == 'q':
            break
        else:
            price = float(price)

        if (price < 0):
            print("Error: purchase price must be non-negative.")

        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

        if price == 'q':
            quit()
        else:
            price = int(float(price) * 100)

        payment = input("Input dollars paid (int): ")

        if payment == 'q':
            break
        else:
            payment = int(float(payment) * 100)

        if (payment < 0):
            print("Error: purchase price must be non-negative.")
    else:
        print("Error: insufficient payment.")
        payment = int(float(input("Input dollars paid (int): ")) * 100)