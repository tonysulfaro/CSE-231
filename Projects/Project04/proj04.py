#########################################################################
# Project 04
# Pattern Recognizer
#
#
#
#
#
#
#########################################################################

def get_ch():
    # prompt for the input in a loop
    ch = input("Enter a character or press the Return key to finish: ")

    # in case of invalid input, print the following error message
    while len(ch) > 1:
        print("Invalid input, please try again.")
        ch = input("Enter a character or press the Return key to finish: ")

    # return the ch at the end
    if len(ch) == 1 or ch == "":
        return ch


def find_state(state, ch):
    pass


def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    # initialize the variables, for example:
    string = ""

    # call the functions in a loop
    while get_ch() != "!":
        get_ch()
        find_state()

    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    print("You are laughing.")
    print("You are not laughing.")


main()