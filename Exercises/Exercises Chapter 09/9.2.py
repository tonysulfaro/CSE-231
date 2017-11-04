import string

def open_file():
    fpointer = open('example.txt')
    return fpointer


def main():
    dictlist = []
    fp = open_file()
    dict_of_words = dict()
    # loop to iterate over lines in file
    for line in fp:
        word_list = line.split()

        for word in word_list:
            word = word.strip().strip(string.punctuation).lower()

            if word not in dict_of_words:
                dict_of_words[word] = 0

            dict_of_words[word] += 1

    for key, value in dict_of_words.items():
        temp = (key, value)
        dictlist.append(temp)
    print(sorted(dictlist))


main()