# add_to_dict() goes here:


# remove_from_dict() goes here


# find_key() goes here


def main():
    more = True
    dictt = {}
    dictlst = []
    while more:
        print("Menu: ")
        choice = input("add(a), remove(r), find(f): ")
        if choice.lower() == "a":
            key = input("Key: ")
            value = input("Value: ")
            dictt = add_to_dict(dictt, key, value)
        elif choice.lower() == "r":
            key = input("key to remove: ")
            dictt = remove_from_dict(dictt, key)
        elif choice.lower() == "f":
            key = input("Key to locate: ")
            find_key(dictt, key)
        else:
            print("Invalid choice.")

        do_more = input("More (y/n)? ")
        if do_more.lower() != 'y':
            more = False
    if dictt:
        for key, value in dictt.items():
            temp = (key, value)
            dictlst.append(temp)
        print(sorted(dictlst))


main()