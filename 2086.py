"""Leia uma sequência de 1000 inteiros.

Leia outro inteiro N, e seu programa deve imprimir quantas vezes o inteiro N aparece nos 1000 anteriores.

O programa para quando o primeiro inteiro dos 1000 for igual a -1."""
while True:
    primeiro = int(input())
    lista = []
    if primeiro == -1:
        break
    else:
        lista.append(primeiro)
    for i in range(999):
        lista.append(int(input()))
    numero = int(input())
    print(f'{numero} appeared {lista.count(numero)} times')
