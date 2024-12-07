a = int(input('informe um número: '))
def primo(n):
    if a <= 1:
        return False  
    cont = 0
    for i in range(1, a + 1): 
        if a % i == 0:
            cont += 1
    if cont == 2: 
        return True
    else:
        return False
print(primo(a))