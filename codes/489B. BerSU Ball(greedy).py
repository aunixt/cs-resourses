n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]

a.sort()
b.sort()

cnt = 0
for i in range(n):
    for j in range(m):
        if abs(a[i] - b[j]) <= 1:
            b[j] = 1000
            cnt += 1
            break

print(cnt)