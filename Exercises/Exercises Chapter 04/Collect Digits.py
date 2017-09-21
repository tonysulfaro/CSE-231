s = input("Input a string: ")
digits = ""

for i,ch in enumerate(s):
    if ch.isdigit():
        digits += ch
print(digits)