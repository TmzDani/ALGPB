Vet1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
Vet2 = [2, 4, 6, 8, 10, 12, 14, 16]
Vet3 = []
i = 0
while i < len(Vet1) or i < len(Vet2):                
    if i <len(Vet1) and i < len(Vet2):                  
        Vet3.append(Vet1[i] + Vet2[i])
    elif i < len(Vet1):                               
        Vet3.append(Vet1[i])                           
    else:
        Vet3.append(Vet2[i])                            
    i += 1
print(Vet3)