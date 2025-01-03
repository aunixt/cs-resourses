t, k = map(int, input().split())
ans = []
dp = [1] * 100001
for i in range(k, 100001):
    dp[i] = (dp[i-1] + dp[i-k]) % 1000000007
the_sum = [0] * 100001
for i in range(1, 100001):
    the_sum[i] = (the_sum[i-1] + dp[i]) % 1000000007
for _ in range(t):
    l, r = map(int, input().split())
    ans.append((the_sum[r] - the_sum[l-1]) % 1000000007)
print(*ans, sep = '\n')