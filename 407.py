while True:
    try:
        ns = a, b = [int(i) for i in input().split()]
    except EOFError:
        break
    ns.sort()
    df = ns[1] - ns[0]
    if df >= 1000:
        ns[0] += (df // 4)
        ns[1] -= (df // 4)
    mx = 1
    for n in range(ns[0], ns[1] + 1):
        c = 1
        while n != 1:
            n = (n * 3 + 1) if n % 2 == 1 else (n // 2)
            c += 1
        if c > mx:
            mx = c
    print(f'{a} {b} {mx}')