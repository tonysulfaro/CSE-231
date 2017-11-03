##function 'return_list' goes here
def return_list(the_string):

    new_list = []

    the_string = the_string.replace(" ",",")
    the_string = the_string.split(",")

    if len(the_string) == 1:
        return the_string[0]
    else:

        for x in range(len(the_string)):

            new_list.append(the_string[x])

        return new_list


def main():
    the_string = input("Enter the string: ")
    result = return_list(the_string)
    print(result)


main()