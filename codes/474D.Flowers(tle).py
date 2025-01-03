t, k = map(int, input().split())
left = []
right = []
n = 0
for _ in range(t):
    l, r = map(int,input().split())
    left.append(l)
    right.append(r)
    n = max(n, r)
m = n // k
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, n+1):
    dp[0][i] = 1
for i in range(1, m+1):
    dp[i][k*i] = 1
for i in range(1, n+2-k):
    dp[1][k-1+i] = i
for i in range(2, m+1):
    for j in range(k*i+1, n+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j-k]) % 1000000007
ans = [0] * (n+1)
for i in range(m+1):
    for j in range(n+1):
        ans[j] = (dp[i][j] + ans[j]) % 1000000007
for i in range(t):
    l, r = left[i], right[i]
    print((sum(ans[l:r+1])) % 1000000007)
print(ans)