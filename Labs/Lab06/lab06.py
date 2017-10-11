fp = open("scores.txt")
counter = 0

student_list = []
total_list = [0,0,0,0]





print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

for line in fp:
    counter += 1

    line = line.strip("\n").strip()
    line = line.split()

    name = line[0] + " " + line[1]
    exam1 = int(line[2])
    exam2 = int(line[3])
    exam3 = int(line[4])
    exam4 = int(line[5])
    average = (exam1+exam2+exam3+exam4)/4
    average = round(average,2)

    total_list[0] += exam1
    total_list[1] += exam2
    total_list[2] += exam3
    total_list[3] += exam4

    tuple = (name,exam1,exam2,exam3,exam4,average)
    student_list.append(tuple)

student_list_sorted = sorted(student_list)

for item in student_list_sorted:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(item[0], item[1], item[2], item[3], item[4], item[5]))

mean_list = [total_list[0]/counter,total_list[1]/counter,total_list[2]/counter,total_list[3]/counter]

print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",mean_list[0], mean_list[1], mean_list[2], mean_list[3]))

