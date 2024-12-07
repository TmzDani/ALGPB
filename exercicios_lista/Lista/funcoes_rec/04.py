def mdc(x, z):
    if z == 0:
        return x
    else:
        return mdc(z, x % z)

def main():
    x = int(input("Informe o primeiro número (x): "))
    z = int(input("Informe o segundo número (z): "))
    resultado = mdc(x, y)
    print(f"O MDC de {x} e {z} é: {resultado}")
if __name__ == "__main__":
    main()
