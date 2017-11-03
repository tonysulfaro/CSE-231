# sort_list() function goes here
a_list = list()

def sort_list(the_list):
    global a_list
    a_list = sorted(the_list)

def main():
    # loop to accept integers until an empty string is entered goes here
    user_input = input()


    while user_input != '':
        try:
            user_input = int(user_input)
            a_list.append(user_input)
        except(TypeError, ValueError):
            print("You can't enter non-numbers")
            quit()
        user_input = input()


    ######Do not modify this part######
    print(a_list)
    sort_list(a_list)
    print(a_list)
    ######Do not modify this part######
    ######main() ends here


main()