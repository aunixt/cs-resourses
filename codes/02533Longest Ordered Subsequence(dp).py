n = int(input())
ls = [int(x) for x in input().split()]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))