print("\nWelcome to change-making program.")

quarters = 10
dimes = 10
nickels = 10
pennies = 10

while True:

    print("\nStock: {} quarters, {} dimes, {} nickles, and {} pennies".format(
        quarters, dimes, nickels, pennies))

    price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    payment = input("Enter the payment received in (xx.xx) format or 'q' to quit: ")

    if price.isdigit() and price > 0:
        price = int(float(price)*100)
    else:
        print("The value you entered is not a number or negative, please enter a valid value.")
        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

    if payment.isdigit() and payment > 0:
        payment = int(float(price) * 100)
    else:
        print("The value you entered is not a number or negative, please enter a valid value.")
        payment = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

    # if user enters 'q', halt the program
    if price == 'q' or payment == 'q':
        break

change = payment - price
print(change)
quartersBack = change // quarters
temp = change - quartersBack * quarters
dimesBack = temp // dimes
tempd = temp - dimesBack * dimes
nickelsBack = temp // nickels
tempn = tempd - nickelsBack * nickels
penniesBack = tempn // pennies
tempp = tempn - penniesBack * pennies

print("The change back is:", quartersBack, "quarters",dimesBack, "dimes", nickelsBack, "nickels and",penniesBack, "pennies.")

