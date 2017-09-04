import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

x1 = float(x1_str)
x2 = float(x2_str)
y1 = float(y1_str)
y2 = float(y2_str)

# convert strings to ints
d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("d =",d)  # do not change this line