# assume a word has at least one vowel
vowels = "aeiou"
vowelCount = 0
consonantCount = 0
vowelString = ""
consonantString = ""
index = 0

word = input("Enter a word.")
word = word.lower()

# your code goes here
while vowelCount < 5 and consonantCount < 5:

    for i, ch in enumerate(word):
        if ch in vowels:
            if ch not in vowelString:
                vowelString += ch
        if ch in vowels:
            index = i

    for i, ch in enumerate(word[index+1:]):

        if ch not in consonantString:
            consonantString += ch

    vowelCount = len(vowelString)
    consonantCount = len(consonantString)

    if vowelCount >= 5 or consonantCount >= 5:
        break

    word = input("Enter a word.")
    word = word.lower()

# here are two lines of the output -- you need to add a third line
# print vowel and consonant string and their lengths through formatting
print("\n" + "=" * 12)
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels", "length", "consonants", "length"))
print("{:8s}{:<7d} | {:12s}{:<7d}".format(vowelString, len(vowelString), consonantString, len(consonantString)))