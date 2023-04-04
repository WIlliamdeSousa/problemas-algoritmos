o = input()
valores = []
for i in range(12):
    for j in range(12):
        n = float(input())
        if i > j:
            valores.append(n)
r = sum(valores)
if o == 'M':
    r = r / valores.__len__()
print(f'{r:.1f}')
