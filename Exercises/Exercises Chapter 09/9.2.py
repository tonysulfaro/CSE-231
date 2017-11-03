def open_file():
    fpointer = open('example.txt')
    return fpointer


def main():
    dictlist = []
    fp = open_file()
    # loop to iterate over lines in file

    for key, value in dict_of_words.items():
        temp = (key, value)
        dictlist.append(temp)
    print(sorted(dictlist))


main()