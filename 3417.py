while True:
    numero = int(input())
    numeros = []
    if numero == -1:
        break
    for i in range(10):
        numeros.append(int(input()))
    print(f'{numero} appeared {numeros.count(numero)} times')
