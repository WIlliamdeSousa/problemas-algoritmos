n = int(input())
bispos = []
dd1 = dict()
dd2 = dict()
for i in range(n):
    x, y = [int(j) for j in input().split()]
    d1 = x - y
    d2 = x + y
    try:
        dd1[d1] += 1
    except KeyError:
        dd1[d1] = 1
    try:
        dd2[d2] += 1
    except KeyError:
        dd2[d2] = 1
    bispos.append((d1, d2))
dominantes = 0
for bispo in bispos:
    if dd1[bispo[0]] == 1 and dd2[bispo[1]] == 1:
        dominantes += 1
print(dominantes)