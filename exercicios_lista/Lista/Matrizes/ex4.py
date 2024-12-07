matrizA = [
    [8, -1],
    [-1, 8]
]

oposta = []

for i in range(len(matrizA)):
    linha_oposta = []
    for j in range(len(matrizA[i])):
        linha_oposta.append(-matrizA[i][j]) 
    oposta.append(linha_oposta) 

for linha in oposta:
    print(linha)