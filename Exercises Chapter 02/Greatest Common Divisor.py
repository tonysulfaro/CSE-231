m = int(input("Input the first integer: "))
n = int(input("Input the second integer: "))
gcd = 0
counter = 0

for x in range(m+n):
    counter += 1
    if m%counter == 0 and n%counter ==0:
        gcd = counter
print(gcd)