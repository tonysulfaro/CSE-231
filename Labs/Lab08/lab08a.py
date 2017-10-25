
import string
from operator import itemgetter


def add_word( word_map, word ):

    # if the word isnt in the word map, add it in and set count to 0
    if word not in word_map:
        word_map[ word ] = 0

    # increment word count for that word by 1
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        #split the word on a space
        word_list = line.split()

        for word in word_list:

            #add word to word list
            word = word.strip().strip(string.punctuation).lower()
            if word != "":
                add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    # for each word and its count in the wordmap
    # append it onto the word list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    word_list = sorted(word_list, reverse= True)

    # YOUR COMMENT
    freq_list = sorted( word_list, key=itemgetter(1), reverse= True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        in_file = open( "document1.txt", "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


