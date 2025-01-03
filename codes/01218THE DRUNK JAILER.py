t = int(input())
for _ in range(t):
    n = int(input())
    dp = [True]*n
    for i in range(1, n+1):
        j = 1
        while i*j <= n:
            dp[i*j - 1] = not dp[i*j - 1]
            j += 1
    print(dp.count(False))