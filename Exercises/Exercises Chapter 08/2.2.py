# sort_list() function goes here
def sort_list(a_list):
    return sorted(a_list)


def main():

    a_list = []

    # loop to accept integers until an empty string is entered goes here
    user_input = input(" ")
    while user_input != "":
        try:
            user_input = int(user_input)
            a_list.append(user_input)
        except (ValueError, TypeError):
            print("That's not an Integer.")
        user_input = input(" ")

    ######Do not modify this part######
    print(a_list)
    a_list = sort_list(a_list)
    print(a_list)
    ######Do not modify this part######
    ######main() ends here


main()