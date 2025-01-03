n = int(input())
nums = [int(x) for x in input().split()]
max_num = max(nums)
count = [0]*(max_num+1)
for i in nums:
    count[i] += 1
dp = [0]*(max_num+1)
dp[1] = count[1]
for i in range(2,max_num+1):
    dp[i] = max(dp[i-1],dp[i-2]+i*count[i])
print(dp[max_num])
