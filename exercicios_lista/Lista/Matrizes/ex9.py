matriz = [
    [0, 2, 11, 6, 15, 11, 1],
    [2, 0, 7, 12, 4, 2, 15],
    [11, 7, 0, 11, 8, 3, 13],
    [6, 12, 11, 0, 10, 2, 1],
    [15, 4, 8, 10, 0, 5, 13],
    [11, 2, 3, 2, 5, 0, 14],
    [1, 15, 13, 1, 13, 14, 0]
]

cidade1 = int(input("Informe a cidade  N° 1(1-7): ")) - 1
cidade2 = int(input("Informe a cidade  N° 2(1-7): ")) - 1

print(f"Tempo entre N°1 {cidade1 + 1} e N°2 {cidade2 + 1}: {matriz[cidade1][cidade2]} horas")