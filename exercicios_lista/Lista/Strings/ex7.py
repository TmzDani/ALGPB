text= input("Informe uma frase: ")

text_invert = ''.join(char.upper() if char.islower() else char.lower() for char in frase)

print("Saída:", text_invert)