import string
#build_wordlist() function goes here
def build_wordlist(fp):
    word_list = []

    for line in fp:

        line = line.strip().strip(string.punctuation).lower()
        line = line.split(" ")
        for item in line:
            if item in word_list:
                pass
            else:
                word_list.append(item)

    return word_list



def main():
    infile = open("test.txt", 'r')
    word_list = sorted(build_wordlist(infile))
    new_wordlist = sorted(word_list)
    print(word_list)
main()