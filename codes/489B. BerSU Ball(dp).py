n = int(input())
boys = sorted(map(int, input().split()))
m = int(input())
girls = sorted(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if abs(boys[i - 1] - girls[j - 1]) <= 1:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[n][m])