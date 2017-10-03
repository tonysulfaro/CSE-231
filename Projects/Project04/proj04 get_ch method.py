def get_ch():
    # prompt for the input in a loop
    ch = input("Enter a character or press the Return key to finish: ")
    ch = str(ch)

    # in case of invalid input, print the following error message
    if len(ch) > 1:
        print("Invalid input, please try again.")
        get_ch()
    elif len(ch) == 1 or ch == "":
        return ch
    else:
        get_ch()


while True:
    ch = str(get_ch())
    print(ch)