import bisect
n = int(input())
ls = [int(x) for x in input().split()]
dp = [1e9]*n
for i in ls:
    dp[bisect.bisect_left(dp,i)] = i
print(bisect.bisect_left(dp,1e8))