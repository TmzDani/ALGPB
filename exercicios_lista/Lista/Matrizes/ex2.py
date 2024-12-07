matriz=[
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4,5],
    [1,2,3,4,5,6]
]
soma=0
for linha in matriz:
    soma+= linha[0]
print (soma)
produto = 1
for coluna in matriz[0]:
    produto *= produto
print(produto)
somaT =0
for todos in matriz:
    for elemento in todos:
        somaT+=elemento
print(somaT)
produtoD=1
for diagonal in range(len(matriz)) :
    produtoD*=matriz[diagonal][diagonal]
print(produtoD)