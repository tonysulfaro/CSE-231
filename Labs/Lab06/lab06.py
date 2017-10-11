fp = open("scores.txt")

student_list = []

print("{:20s}{:6s}{:6s}{:6s}{:6s}{:6s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
for line in fp:
    line = line.replace(" ", "")
    student_list.__add__(list(line))
    print(student_list)
