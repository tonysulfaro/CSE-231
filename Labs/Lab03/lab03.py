vowels = "aeiou"

word = input("Enter a word ('quit' to quit): ")
word = word.lower()
print(word)

if word == 'quit':
    quit()

while word != 'quit':

    word = input("Enter a word ('quit' to quit): ")
    word = word.lower()
    print(word)


# Error message used in Mimir test
# print("Can't convert empty string.  Try again.")