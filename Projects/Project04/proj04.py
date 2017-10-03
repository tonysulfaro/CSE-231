#########################################################################
# Project 04
# Pattern Recognizer
#
# get next char method
#   while true for user input
#       input
#       if input is invalid print error
#       else return the value
#
# find state given previous state
#   if state = x then check other conditions for y
#       state = x
#       return state
#
# main method
#   print welcome message/instructions
#   initialize variables
#   call functions in a loop
#       get ch
#       append result onto input string
#       find state to be passed into state function
#   when user enters in enter "null"
#       exit the program and print if they are laughing and the string
#########################################################################

#gets user input as individual character
def get_ch():

    # prompt for the input in a loop
    while True:

        ch = input("Enter a character or press the Return key to finish: ")

        # in case of invalid input, print the following error message
        if len(ch) > 1:
            print("Invalid input, please try again.")
        elif len(ch) == 1 or ch == "":
            return ch
        else:
            print("Invalid input, please try again.")

#finds state of character entered
def find_state(state, ch):

    #Start of program
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

    #given ch is already a or o
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

    #given last one was '!'
    if state == 4:
        if ch == '!':
            state = 4
            return state
        else:
            state = 5
            return state

    #state is failed (not laughing)
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

        if ch == '':
            break

        string += ch
        state = find_state(state,ch)

    # when user enters an empty string, you should print the results
    print("\nYou entered", string)
    if state == 4:
        print("You are laughing.")
    else:
        print("You are not laughing.")


main()