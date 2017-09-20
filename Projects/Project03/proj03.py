# assume a word has at least one vowel
vowels = "aeiou"
vowelCount = 0
consonantCount = 0
vowelString = ""
consonantString = ""

word = input("Enter a word.")
word = word.lower()

# your code goes here
while len(vowelString) < 5 or len(consonantString) < 5:

    for i, ch in enumerate(word):
        if ch in vowels:
            if ch not in vowelString:
                vowelCount += 1
                vowelString += ch
        else:
            if ch not in consonantString:
                consonantCount += 1
                consonantString += ch

    print("\n" + "=" * 12)
    print("{:8s}{:7s} | {:12s}{:7s}".format("vowels", "length", "consonants", "length"))
    print(vowelString, vowelCount, consonantString, consonantCount)

    word = input("Enter a word.")
    word = word.lower()

# here are two lines of the output -- you need to add a third line
print("\n"+"="*12)
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels","length","consonants","length"))
print(vowelString,vowelCount,consonantString,consonantCount)