# add_to_dict() goes here:
def add_to_dict(dictt, key, value):
    data = {key: value}
    if key not in dictt:
        dictt.update(data)
    else:
        print("Error. Key already exists.")
    return dictt


# remove_from_dict() goes here
def remove_from_dict(dictt, key):
    try:
        del dictt[key]
    except KeyError:
        print("No such key exists in the dictionary.")
    return dictt


# find_key() goes here
def find_key(dictt, key):
    try:
        print("Value:",dictt[key])
    except KeyError:
        print("Key not found.")
    return dictt


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