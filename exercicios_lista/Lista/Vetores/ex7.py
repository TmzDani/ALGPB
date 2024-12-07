matricula = []

for c in range(100):
    num = int(input('Informe matricula: '))

    if num in matricula:
        print('Esse valor de matricula já existe, informe outro que seja numero')
    else:
        matricula.append(num)

print(matricula)