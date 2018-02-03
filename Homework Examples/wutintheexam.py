B, C, D = 0, 0, 0

for A in [0, 1, 3, 5, 7, 9]:
    if A:
        if A % 2 == A:
            B += 1
        else:
            C += 1
        if A % 3 == 0:
            D += 1
            break

print( A ) # Line 1
print( B ) # Line 2
print( C ) # Line 3
print( D ) # Line 4