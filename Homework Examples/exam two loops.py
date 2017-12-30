print([a*b for a in range(2) for b in range(2)])

for a in range(2):
    print('outer')
    for b in range(2):
        print('inner')
        print(a*b)