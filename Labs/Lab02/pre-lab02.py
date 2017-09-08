
A,B,C = 0,0,0

for N in range(11):
    if N%2 == 0:
        A += 1
    elif N%3 == 0:
        B += 1
    else:
        C += 1
print("A =", A) # Line 1
print("B =", B) # Line 2
print("C =", C) # Line 3
print("N =", N) # Line 4