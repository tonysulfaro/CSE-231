#physically hurts to have entire alphabet as a variable
letters = "abcdefghijklmnopqrstuvwxyz"

# palindrome function definition goes here
def palindrome(in_str):

    string = ""
    in_str = in_str.lower()

    for i,ch in enumerate(in_str):
        if ch in letters:
            string += ch

    if string == string[::-1]:
        return True
    else:
        return False

in_str = input("Enter a string: ")

print('"{:s}" is '.format(in_str),end='')
if not palindrome(in_str):
    print("not ", end = '')
print("a palindrome.")