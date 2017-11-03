dictlist = []
#declare variables
#loop needed
input("Name: ")
input("Number: ")
##add name and number to dictionary
input('More data (y/n)? ')
#if more data, then repeat

for key, value in the_dict.items():  #we store the dictionary in a list, then sort and print
    temp = (key,value)
    dictlist.append(temp)
print(sorted(dictlist))
