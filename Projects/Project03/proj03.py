# assume a word has at least one vowel
vowels = "aeiou"
count = 0

word = input("Enter a word.")
word = word.lower()

# your code goes here
while word != 'quit' and count < 5:
    print(word)


# here are two lines of the output -- you need to add a third line
# print("\n"+"="*12)
# print("{:8s}{:7s} | {:12s}{:7s}".format("vowels","length","consonants","length"))