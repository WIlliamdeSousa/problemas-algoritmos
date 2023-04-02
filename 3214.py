st = int(input())
for i in [86400, 3600, 60, 1]:
    print(st // i)
    st %= i