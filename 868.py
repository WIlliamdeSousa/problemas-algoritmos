n, d = [int(i) for i in input().split()]
ns = []
for i in range(n):
    ni = int(input())
    if ni % 10 == d:
        ns.append(ni)
    else:
        ns.append(-1)
ns.sort(reverse=True)
for i in ns[0:5][::-1]:
    print(i)