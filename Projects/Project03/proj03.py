# assume a word has at least one vowel
vowels = "aeiou"
vowelString = ""
consonantString = ""
index = 0

word = input("Input a word: ")
word = word.lower()

# your code goes here
while len(vowelString)< 5 and len(consonantString) < 5:

    for i, ch in enumerate(word):
        if ch in vowels:
            if ch not in vowelString:
                vowelString += ch
        if ch in vowels:
            index = i

    for i, ch in enumerate(word[index+1:]):

        if ch not in consonantString:
            consonantString += ch

    if len(vowelString) >= 5 or len(consonantString) >= 5:
        break

    word = input("Input a word: ")
    word = word.lower()

# here are two lines of the output -- you need to add a third line
# print vowel and consonant string and their lengths through formatting
print("\n" + "=" * 12)
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels", "length", "consonants", "length"))
print("{:8s}{:<7d} | {:12s}{:<7d}".format(vowelString, len(vowelString), consonantString, len(consonantString)))