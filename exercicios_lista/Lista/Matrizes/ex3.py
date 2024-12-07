matrizA = [
    [-20, 2, 5, 7],
    [5, 3, 2, 8]
]
matrizB = [
    [0, 8, 4, -2],
    [0, 8, 3, -6]
]
soma = []

for i in range(len(matrizA)):
    linha_soma = []  
    for j in range(len(matrizA[i])):
        linha_soma.append(matrizA[i][j] + matrizB[i][j])  
    soma.append(linha_soma) 

for linha in soma:
    print(linha)