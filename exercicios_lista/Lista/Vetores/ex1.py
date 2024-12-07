vet = []
soma = 0
maior = 0
menor = float('inf')         

for c in range(100):
    num = float(input('Informe um numero: '))
    vet.append(num)

for num in vet:
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / len(vet)
print(vet)
print(maior)
print(menor)
print(media)
print(soma)