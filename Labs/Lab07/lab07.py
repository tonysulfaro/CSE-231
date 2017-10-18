def open_file():
    '''Remember to put a docstring here'''
    while True:
        file_name = input("Input a file name: ")
        try:

            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            continue
    return fp


def main():

    count = [0 for i in range(9)]
    percentages = [0 for i in range(9)]
    expected_percentages = ['30.1','17.6','12.5','9.7','7.9','6.7','5.8','5.1','4.6']

    fp = open_file()

    for line in fp:

        line = line.strip()

        try:
            number = int(line)
        except (TypeError, ValueError):
            pass

        try:
            number = int(str(line[0]))
        except ValueError:
            pass

        index = number - 1
        count[index]+= 1


    line_count = sum(count)

    print("Digit Percent Benford")
    for x in range(len(count)):
        percentages[x] = (count[x]/line_count)*100
        print("{:3s} {:>10.1f}% ({:>5s}%) ".format(str(x+1)+":",percentages[x],expected_percentages[x]))


main()