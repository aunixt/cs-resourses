t = int(input())
for _ in range(t):
    alpha = int(input())
    if 360 % (180 - alpha) == 0 and  360 // (180 - alpha) >= 3:
        print('YES')
    else:
        print('NO')