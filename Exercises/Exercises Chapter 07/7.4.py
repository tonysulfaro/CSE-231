# list_to_tuple function goes here
def list_to_tuple(a_list):

    a_tuple = ()

    int_list = []

    for item in a_list:

        try:
            item = int(item)

            int_list.append(item)
        except (ValueError, TypeError):
            print("Error. Please enter only integers.")
            quit()

    return tuple(int_list)


def main():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    tup = list_to_tuple(a_list)
    print(tup)


main()