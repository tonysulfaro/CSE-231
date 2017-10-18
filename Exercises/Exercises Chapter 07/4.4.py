# list_to_tuple function goes here
def list_to_tuple(a_list):

    a_tuple = ()

    int_list = ""

    for item in a_list:

        try:
            item = int(item)
            print(item)
            int_list += str(item)
        except (ValueError, TypeError):
            print("Error. Please enter only integers.")
    a_tuple(int_list)
    return a_tuple


def main():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    list_to_tuple(a_list)


main()