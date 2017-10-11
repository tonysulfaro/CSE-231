fp = open("scores.txt")

student_list = []

print("{:20s}{:6s}{:6s}{:6s}{:6s}{:6s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

for line in fp:
    line = line.strip("\n").strip()
    line = line.split()

    name = line[0] + " " + line[1]
    exam1 = int(line[2])
    exam2 = int(line[3])
    exam3 = int(line[4])
    exam4 = int(line[5])
    average = round(((exam1+exam2+exam3+exam4)/4.0), 2)

    print(line)

    tuple = (name,exam1,exam2,exam3,exam4,average)
    student_list.append(tuple)

student_list_sorted = sorted(student_list)

for item in student_list_sorted:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:6f}".format(item[0], item[1], item[2], item[3], item[4], item[5]))
