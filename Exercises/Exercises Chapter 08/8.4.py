#game_of_eights() function goes here
def game_of_eights(a_list):
    last_num = 0
    for item in a_list:
        try:
            int(item)
        except (ValueError, TypeError):
            print("Error. Please enter only integers.")
            quit()

    for item in a_list:
        try:
            item = int(item)
            if item == last_num:
                return True

        except (ValueError, TypeError):
            print("Error. Please enter only integers.")
            break
        last_num = item
    return False
def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    result = game_of_eights(a_list)
    print(result)

main()