import string
from operator import itemgetter


def add_word(word_map, name, score):
    # if the word isnt in the word map, add it in and set count to 0
    try:
        score = int(score)

        if name not in word_map:
            word_map[name] = 0

        # increment word count for that word by 1
        word_map[name] += score

    except (ValueError, TypeError):
        pass


def build_map(in_file, word_map):
    for line in in_file:

        # split the word on a space
        line = line.split()

        #print(line)
        name = line[0]
        score = line[1]

        add_word(word_map, name, score)

def display_map(word_map):
    word_list = list()

    # for each word and its count in the wordmap
    # append it onto the word list
    for word, count in word_map.items():
        word_list.append((word, count))

    word_list = sorted(word_list)

    # YOUR COMMENT
    freq_list = sorted(word_list)

    print("\n{:15s}{:5s}".format("Name", "Total"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def open_file(name):
    try:
        in_file = open(name, "r")

    except IOError:
        print("\n*** unable to open file ***\n")
        in_file = None

    return in_file


word_map = dict()
in_file = open_file("data1.txt")

if in_file != None:
    build_map(in_file, word_map)

in_file = open_file("data2.txt")

if in_file != None:
    build_map(in_file, word_map)
    display_map(word_map)
    in_file.close()


