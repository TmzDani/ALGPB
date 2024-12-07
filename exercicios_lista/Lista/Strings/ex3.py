cod = input("Informe um código de 5 algarismos: ")


if len(cod) == 5 and cod.isdigit():
   
    A, B, C, D, E = map(int, cod)
    
   
    S = 6 * A + 5 * B + 4 * C + 3 * D + 2 * E
    
    
    DigitoV = S % 7
    
 
    print(f"O dígito verificador (módulo 7) é: {DigitoV}")
else:
    print("Código inválido! Por favor, APENAS 5 dígitos.")