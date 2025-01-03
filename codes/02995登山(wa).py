n = int(input())
h = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    dp = [0] * n
    s = h[i]
    max1 = 0
    max2 = 0
    for j in range(i-1, -1, -1):
        for m in range(1, i-j+1):
            if h[j] < h[j+m] and h[j] < s:
                dp[j] = max(dp[j], dp[j+m] + 1)
        max1 = max(max1, dp[j])
    for k in range(i+1, n, 1):
        for m in range(1, k-i+1):
            if h[k] < h[k-m] and h[k] < s:
                dp[k] = max(dp[k], dp[k-m] + 1)
        max2 = max(max2, dp[k])

    print(dp)
    ans = max(ans, max1 + max2 + 1)

print(ans)

