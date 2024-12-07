Notas = [9.8, 7.5, 8.5, 6, 7]


maior = Notas[0]
menor = Notas[0]
soma = 0

for Nota in Notas:             
    if Nota > maior:
        maior = Nota            
    if Nota < menor:
        menor = Nota            
    soma += Nota                


media = (soma - maior - menor)/(len(Notas) - 2)  
print('A média é {}'.format(media))
print('A maior  {}'.format(maior))
print('A menor  {}'.format(menor))