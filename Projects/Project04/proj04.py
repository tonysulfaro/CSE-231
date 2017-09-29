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

state = ''
stateString = ''

def get_ch():
    # prompt for the input in a loop
    ch = input("Enter a character or press the Return key to finish: ")

    # in case of invalid input, print the following error message
    if len(ch) > 1:
        print("Invalid input, please try again.")
        get_ch()

    # return the ch at the end
    elif len(ch) == 1 or ch == "":
        state = ch
        print(stateString)
        return ch
    else:
        get_ch()


def find_state(state, ch):
    #if state ==
    pass


def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    # initialize the variables, for example:
    string = ""

    # call the functions in a loop
    while get_ch() != "!":
        find_state(state,get_ch())

    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    print("You are laughing.")
    print("You are not laughing.")


main()