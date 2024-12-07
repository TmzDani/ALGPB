ordem = int(input("Informe a ordem da matriz: "))
identidade = [[1 if i == j else 0 for j in range(ordem)] for i in range(ordem)]

print("Matriz informada:")
for linha in identidade:
    print(linha)