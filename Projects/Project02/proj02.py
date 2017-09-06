print("\nWelcome to change-making program.")

quarters = 10
dimes = 10
nickels = 10
pennies = 10

while True:

    print("\nStock: {} quarters, {} dimes, {} nickles, and {} pennies".format(
        quarters, dimes, nickels, pennies))

    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")

    # if user enters 'q', halt the program
    if in_str == 'q':
        break

    # Fill in the good stuff here instead of the following print
    print("Testing:", in_str)

change = payment - price
print(change)
quartersBack = change // quarters
temp = change - quartersBack * quarters
dimesBack = temp // dimes
temp = temp - dimesBack * dimes
nickelsBack = temp // nickels
temp = temp - nickelsBack * nickels
penniesBack = temp // pennies
temp = temp - penniesBack * pennies

print("The change back is:", quartersBack, "quarters",dimesBack, "dimes", nickelsBack, "nickels and",penniesBack, "pennies.")

