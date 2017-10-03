def get_ch():
    # prompt for the input in a loop
    while True:
        ch = input("Enter a character or press the Return key to finish: ")
        ch = str(ch)

        # in case of invalid input, print the following error message
        if len(ch) > 1:
            print("Invalid input, please try again.")
        elif len(ch) == 1 or ch == "":
            return ch
        else:
            print("Invalid input, please try again.")


while True:
    ch = str(get_ch())
    print(ch)