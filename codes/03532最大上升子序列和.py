n = int(input())
ls = [int(x) for x in input().split()]
dp = ls[:]
for i in range(n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j]+ls[i])
print(max(dp))