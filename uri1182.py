c = int(input())
o = str(input())
s = 0
for i in range(12):
    for j in range(12):
        n = float(input())
        if j == c:
            s += n
if o == 'M':
    print(f'{s/12:.1f}')
else: 
    print(f'{s:.1f}')