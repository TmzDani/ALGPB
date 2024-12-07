#Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
cont = 0
def fib(n):
    global cont
    cont +=1
    if n <= 1:
        return n
    else:
        return fib(n-1)+(n-2)
print(fib(21))
print(cont)