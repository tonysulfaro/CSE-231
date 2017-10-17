# list_to_tuple function goes here
def list_to_tuple(a_list):

    a_tuple = ()

    for item in a_list:

        try:
            item = int(item)
            print(item)
            #a_tuple(item)
        except (ValueError, TypeError):
            print("Error. Please enter only integers.")

    return a_tuple


def main():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    list_to_tuple(a_list)


main()