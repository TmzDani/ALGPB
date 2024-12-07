string1 = input("Informe a primeira string: ").lower().replace(" ", "")
string2 = input("Informe a segunda string: ").lower().replace(" ", "")       

if sorted(string1) == sorted(string2):                
    print("strings são anagramas!")
else:
    print("strings NÃO são anagramas.")