file_str = input("Enter a file to open: ")
Done = False
while not Done:
    try:
        file_obj = open(file_str, 'r')
        print("Opened the file",file_str)    # executed if no error
        Done = True
    except IOError:
        print("File opening failed")         # executed on file open error
        file_str = input("Try again to enter a file to open:")

word_count = 0
for line in file_obj:
    words = line.count(" ") + 1
    word_count += words

file_obj.close()
outfile_str = input("Enter a file to open: ")
Done = False
while not Done:
    try:
        outfile_obj = open(outfile_str, 'w')
        print("Opened the file",outfile_str)    # executed if no error
        Done = True
    except IOError:
        print("File opening failed")         # executed on file open error
        outfile_str = input("Try again to enter a file to open:")

outfile_obj.write("Words: " + str(word_count))
outfile_obj.close()
