dictlist = []
the_dict = dict()
#declare variables

choice = ""
#loop needed
while choice != 'n':
    name = input("Name: ")
    number = input("Number: ")

    #add name and number to dictionary
    the_dict[name] = number

    choice = input('More data (y/n)? ').lower()

#if more data, then repeat

for key, value in the_dict.items():  #we store the dictionary in a list, then sort and print
    temp = (key,value)
    dictlist.append(temp)
print(sorted(dictlist))
