import string
#build_wordlist() function goes here
def build_wordlist(fp):
    word_list = []

    for line in fp:

        line = line.strip().strip(string.punctuation).lower()
        line = line.split(" ")
        if line in word_list:
            pass
        else:
            word_list.append(line)

    return word_list



def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)
    new_wordlist = sorted(word_list)
    print(word_list)
main()