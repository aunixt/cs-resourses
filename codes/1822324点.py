n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    flag = False
    for i in [a, -a]:
        for j in [b, -b]:
            for p in [c, -c]:
                for q in [d, -d]:
                    if i+j+p+q == 24:
                        flag = True
                        break
    print('YES' if flag else 'NO')

