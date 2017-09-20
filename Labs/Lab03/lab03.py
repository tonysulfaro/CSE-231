vowels = "aeiou"

#user input
word = input("Enter a word ('quit' to quit): ")
word = word.lower()

if word == 'quit':
    quit()

#mainloop
while word != 'quit':

    if word[0] in vowels:
        word = word + "way"
    elif word[0] not in vowels and len(word) == 1:
        word = word + 'ay'
    else:
        for i, ch in enumerate(word):
            if ch in vowels:
                word = word[i:] + word[:i] + "ay"
                break

    print(word)

    #user input
    word = input("Enter a word ('quit' to quit): ")
    word = word.lower()