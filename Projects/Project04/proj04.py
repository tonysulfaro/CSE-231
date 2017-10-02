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
    if len(ch) > 1:
        print("Invalid input, please try again.")
        get_ch()

    # return the ch at the end
    elif len(ch) == 1 or ch == "":
        return ch
    else:
        get_ch()


def find_state(state, ch):
    state = 0

    if ch == 'a' or ch == 'o':
        state = 0
        return state
    elif ch == 'h':
        state = 1
        return state
    else:
        state = -1
        return state


def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    # initialize the variables, for example:
    state = 0
    string = ""
    ch = ''

    # call the functions in a loop
    while ch != "!":
        ch = get_ch()
        string += ch
        state = find_state(state,ch)

    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    if state != 3:
        print("You are laughing.")
    else:
        print("You are not laughing.")


main()