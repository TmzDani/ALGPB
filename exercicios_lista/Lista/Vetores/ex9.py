A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10, 12, 14, 16]
C = []

i = 0 
j = 0

while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        C.append(A[i])  
        i += 1          
    else:
        C.append(B[j])  
        j += 1          


C.extend(A[i:])  

C.extend(B[j:])  

print(C)