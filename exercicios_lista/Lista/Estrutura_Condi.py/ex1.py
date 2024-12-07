estado_civil = str(input('informe a letra: '))
estado_civil = estado_civil.upper()
if est_civil == 'S':
    print('Você é solteiro')
elif est_civil == 'C':
    print('Você é Casado')
elif est_civil == 'V':
    print('Você é Viúvo')
elif est_civil == 'D':
    print('Você é divorciado')
elif est_civil == 'E':
    print('Você é Equitado')
else:
    print('error')