import copy
L1 = ['a','b','c']
L2 = [1, 2, L1]
L3 = L2
L4 = copy.deepcopy(L3)

print(L3 is L2)  # Line 1
print(L4 is L2)  # Line 2
print(L4 == L2)  # Line 3
L1[2] = [10, 11]
print(L3)        # Line 4
print(L4)        # Line 5