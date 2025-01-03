T, n = map(int, input().split())
t, w = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    w.append(b)
dp = [([0]+[-float('inf')]*T) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, T+1):
        if j < t[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t[i]] + w[i])
if dp[n][T] == -float('inf'):
    print(-1)
else:
    print(dp[n][T])