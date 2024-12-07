V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
V2 = []
V3 = []
total = len(V)

for c in V:
    if c % 2 == 0:              
        V2.append(c)
    else:
        V3.append(c)

print(V)
print(V2)
print(V3)