# palindrome function definition goes here
import string

def palindrome(in_str):
    string = ""
    for i,ch in enumerate(in_str):
        if ch in string.ascii_letters:
            string += ch
    print(string)
    if string == string[::-1]:
        return True
    else:
        return False

in_str = input("Enter a string: ")

print('"{:s}" is '.format(in_str),end='')
if not palindrome(in_str):
    print("not ", end = '')
print("a palindrome.")