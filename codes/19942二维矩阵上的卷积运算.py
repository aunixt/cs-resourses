m, n, p, q = map(int,input().split())
matrix = [[int(x) for x in input().split()] for _ in range(m)]
core = [[int(x) for x in input().split()] for _ in range(p)]
ans = [[0] * (n+1-q) for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for k in range(p):
            for s in range(q):
                ans[i][j] += matrix[i+k][j+s] * core[k][s]
for x in ans:
    print(*x)