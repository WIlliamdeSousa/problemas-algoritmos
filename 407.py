while True:
    try:
        a, b = [int(i) for i in str(input()).split()]
    except EOFError:
        break
    max = 0
    lista = range(a, b + 1) if a < b else range(b, a + 1)
    for n in lista:
        c = 1
        while True:
            if n == 1:
                break
            c += 1
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
        if c > max:
            max = c
    print(f'{a} {b} {max}')