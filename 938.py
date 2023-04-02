n = 0
for i in range(5):
    if float(input('Digite um valor:\n')) < 0:
        n += 1
print(f'Foram digitados {n} numeros negativos')