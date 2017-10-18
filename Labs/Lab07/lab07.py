def open_file():
    fp = ""

    while True:

        file_name = input("Enter a filename: ")
        try:
            fp = open(file_name)
        except FileNotFoundError:
            print("Error invalid filename.")

def main():
    pass