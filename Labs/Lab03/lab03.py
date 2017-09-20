vowels = "aeiou"

word = input("Enter a word ('quit' to quit): ")
word = word.lower()

if word == 'quit':
    quit()

while word != 'quit':

    if word[0] in vowels:
        word = word + "way"
    else:
        for i, ch in enumerate(word):
            if ch in vowels:
                word = word[i:] + word[:i] + "ay"
                break

    print(word)

    #user input
    word = input("Enter a word ('quit' to quit): ")
    word = word.lower()


