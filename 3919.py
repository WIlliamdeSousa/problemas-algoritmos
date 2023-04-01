n = int(input())
x = []
for i in range(20):
    x.append(int(input()))
    if x[i] == -1:
        break
print(f'{n} aparece {x.count(n)} vezes')
