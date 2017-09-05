Nickels = 10
Dimes = 10
Quarters = 10
Pennies = 10
choice = ""
price = 0
payment = 0

while choice != "q":

    while price <= 0:
        choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
        price = float(choice)
        price = price

        if price < 0:
            print("The price you entered was negative, please enter a positive price.")

    while payment > price:

        payment = float(input("Please enter the payment received in xx.xx format: "))

        if payment < price:
            print("The payment amount is insufficient for the price of the item, "
                  "please pay an amount greater than or equal to the price ", price)