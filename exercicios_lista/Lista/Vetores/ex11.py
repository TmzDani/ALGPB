A = [1, 8, 2, 4, 3, 4, 2, 5, 1]
B = [0, 3, 3, 7, 5, 2, 3, 3, 7]


re = []
ini = 0
total = len(A)



for i in range(total - 1, -1, -1):
    soma = A[i] + B[i] + ini
    re.append(soma % 10)         
    ini = soma // 10       


if ini:
    re.append(ini)


re.reverse()
print(re)