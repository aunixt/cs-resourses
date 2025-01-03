n, m = map(int, input().split())
dp = [1] + [0] * n
for i in range(1, m):
    dp[i] = 2 * dp[i-1]
for i in range(m, n+1):
    dp[i] = 2*dp[i-1] - dp[max(0, i-m-1)]
print(dp[n])