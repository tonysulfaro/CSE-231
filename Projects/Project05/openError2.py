file_str = input("Enter me a file to open: ")

while True:
    try:
        file_obj = open(file_str, 'r')
        print("Opened the file",file_str)    # executed if no error
        break
    except IOError:
        print("File opening failed")         # executed on file open error
        file_str = input("Enter me a file to open: ")  # ask again
        
#print("moving on")                       # always executed

word_count = 0
for line in file_obj:
    words = line.count(" ") + 1
    word_count += words

print("Words:", word_count)
