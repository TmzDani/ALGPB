def somatorio(N):
    if A == 1:
        return 1
    else:
        return NA+ somatorio(A - 1)
def main():
    A = int(input("Digite um número inteiro positivo N: "))
    resultado = somatorio(A)
    print(f"O somatório de 1 até {A} é: {resultado}")


if __name__ == "__main__":
    main()
