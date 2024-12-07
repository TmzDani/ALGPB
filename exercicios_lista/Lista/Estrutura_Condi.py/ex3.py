cod = int(input('Informe o codigo um cliente comum (1), funcionário (2) ou vip (3): '))
val = float(input('Informe o valor da compra: '))
if cod == 2:
    desc = val * 0.10
    tot = val - desc
    print(total)
elif cod == 3:
    desc = val * 0.05
    tot = val - desc
    print(tot)
else:
    print(val)