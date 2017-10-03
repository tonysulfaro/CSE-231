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


def find_state(state, ch):

    if state == 1:
        if ch == 'h':
            state = 1
            return state
        elif ch == 'a' or ch == 'o':
            state = 2
            return state
        else:
            state = 5
            return state

    if state == 2 or state == 3:
        if ch == 'a' or ch == 'o':
            state = 2
            return state
        elif ch == 'h':
            state = 3
            return state
        elif ch == '!':
            state = 4
            return state
        else:
            state = 5
            return state

    if state == 4:
        if ch == '!':
            state = 4
            return state
        else:
            state = 5
            return state

    if state == 5:
        state = 5
        return state


def main():
    print("I can recognize if you are laughing or not.")
    print("Please enter one character at a time.")

    # initialize the variables, for example:
    state = 1
    string = ""
    ch = 'null'

    # call the functions in a loop
    while ch != "":
        ch = get_ch()
        ch = str(ch)

        if ch == '':
            break
        print(string)
        string += ch
        print(string)
        state = find_state(state,ch)

    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    if state == 4:
        print("You are laughing.")
    else:
        print("You are not laughing.")


main()