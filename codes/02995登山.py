n = int(input())
nums = [int(x) for x in input().split()]
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

nums.reverse()
rdp = [1] * n
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            rdp[i] = max(rdp[i], rdp[j] + 1)

rdp.reverse()
ans = 0
for i in range(n):
    ans = max(ans, dp[i] + rdp[i] - 1)
print(ans)
