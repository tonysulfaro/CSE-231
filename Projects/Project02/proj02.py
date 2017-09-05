Nickels = 10
Dimes = 10
Quarters = 10
Pennies = 10
choice = ""
price = 0
payment = 0

while choice != "q":

    # check price and prompt for user input
    if price == 0:
        choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
        price = float(choice)
        if price < 0:
            print("The price you entered was negative or not a number, please try again.")
            choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
            price = float(choice)
    elif price > 0:
        1+2
    else:
        print("The price you entered was negative or not a number, please try again.")
        choice = input("Please enter a price in the form xx.xx or enter q to quit: ")
        price = float(choice)

    #check payment amount and prompt for user input
    if payment == 0:
        payment = float(input("Please enter the payment received in xx.xx format: "))
    elif payment < price:
        print("The payment amount is insufficient for the price of the item, "
              "please pay an amount greater than or equal to the price ", price)
        payment = float(input("Please enter the payment received in xx.xx format: "))
    elif payment >= price:
        print("thanks for payment")
        break
