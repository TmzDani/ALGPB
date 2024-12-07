def fibonacci(A):
    if A == 0:
        return 0
    elif A == 1:
        return 1
    else:
        return fibonacci(A - 1) + fibonacci(A - 2)
def main():
    A = int(input("Informe um número inteiro positivo N para encontrar o N-ésimo termo da sequência Fibonacci: "))
    resultado = fibonacci(A)
    print(f"O {A}-ésimo termo da sequência Fibonacci é: {resultado}")
if __name__ == "__main__":
    main()
