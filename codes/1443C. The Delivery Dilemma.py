t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ls = []
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for i in range(n):
        ls.append((a[i], b[i]))
    ls.sort(reverse = True)
    time = 0
    for i in range(n):
        time += ls[i][1]
        if time >= ls[i][0]:
            time = max(ls[i][0], time - ls[i][1])
            break
    ans.append(time)
print(*ans, sep = '\n')