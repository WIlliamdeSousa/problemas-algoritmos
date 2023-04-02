while True:
    ev1, ev2, at, d = [int(i) for i in input().split()]
    if ev1 == ev2 == at == d == 0:
        break
    cv1 = ev1 // d + (0 if ev1 % d == 0 else 1)
    cv2 = ev2 // d + (0 if ev2 % d == 0 else 1)
