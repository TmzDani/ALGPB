def fatorial(A):
    if A == 0 or A == 1:
        return 1
    else:
        return A * fatorial(A - 1)
def main():
    A = int(input("Informe um número inteiro positivo N: "))
    resultado = fatorial(A)
    print(f"O fatorial de {A} é: {resultado}")
if __name__ == "__main__":
     main()

