Nickels = 10
Dimes = 10
Quarters = 10
Pennies = 10
choice = ""
price = 0.00
payment = 0.00

while choice != "q":
    choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
    price = float(choice)

    if price < 0:
        print("The price you entered was negative, please enter a positive price.")

    payment = float(input("Please enter the payment received in xx.xx format: "))

    if payment < price:
        print("The payment amount is insufficient for the price of the item, "
              "please pay an amount greater than or equal to the price ",price)