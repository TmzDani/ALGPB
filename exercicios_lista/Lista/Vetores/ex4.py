V1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58, 78, 43, 79, 178]
V2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58, 87, 34, 97, 871]
cont = 0

for c in range(15):
    if V1[c] == V2[c]:
        cont += 1
print('É igual até {}'.format(cont))