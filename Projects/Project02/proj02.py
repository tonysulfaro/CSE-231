Nickels = 10
Dimes = 10
Quarters = 10
Pennies = 10
choice = ""
price = 0
payment = 0

while choice != "q":

    if price <= 0:
        choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
        price = float(choice)
    else:
        print("The price you entered was negative or not a number, please try again.")
        choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
        price = float(choice)


while payment > price:

    payment = float(input("Please enter the payment received in xx.xx format: "))

    if payment < price:
        print("The payment amount is insufficient for the price of the item, "
              "please pay an amount greater than or equal to the price ", price)