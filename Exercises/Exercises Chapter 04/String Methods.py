name = input("Input a name: ")
comma = 0

for i,ch in enumerate(name):
    if ch == ",":
        comma = i

formattedName = name[comma+2:comma+3].upper() + ". " + name[:1].upper() + name[1:comma]
print(formattedName)