# list_to_tuple function goes here
def list_to_tuple(a_list):
    a_tuple = ()

    for item in a_list:
        item = int(item)
        try:
            a_tuple = a_tuple(a_list)
        except ValueError:
            print("Error. Please enter only integers.")

def main():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    list_to_tuple(a_list)


main()