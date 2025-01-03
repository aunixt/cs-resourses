dp = [0, 1, 2] + [0] * 1000000
for i in range(3, 1000000):
    dp[i] = (2 * dp[i-1] + dp[i-2]) % 32767
n = int(input())
for _ in range(n):
    k = int(input())
    print(dp[k])
