"""Determinar em um conjuto de 1000 números inteiros, quantas vezes aparece o número N. 

Leia um número N e uma sequência de 1000 inteiros.

O programa deve ler outra sequencia de 1000 números inteiros enquanto N for diferente de -1.

O programa deve parar quando o número N digitado for igual a -1."""
while True:
    try:
        primeiro = int(input())
    except EOFError:
        break
    lista = []
    if primeiro == -1:
        break
    else:
        lista.append(primeiro)
    for i in range(9):
        lista.append(int(input()))
    n = int(input())
    print(f'{n} appeared {lista.count(n)} times')
