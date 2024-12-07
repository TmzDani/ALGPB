a = input('Informe o seu nome: ')
a1 = ''
for i in range(len(a) - 1, -1, -1):         
    a1 += a[i]
a1 = a1.upper()  
print(a1)