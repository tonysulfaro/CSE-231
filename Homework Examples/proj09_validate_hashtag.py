import string

s = "#gern."

s = s[1:]
s = set(s)

print(s.intersection(string.punctuation))

if s.intersection(string.punctuation) != set() or s.intersection(string.digits) != set():
    print("false")
else:
    print("true")