#build_wordlist() function goes here
def build_wordlist(fp):
    word_list = []

    for line in fp:
        line = line.split(" ")
        line = line.replace((",",".",":"),"")



        word_list.append(line)

#find_unique() function goes here

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)
main()