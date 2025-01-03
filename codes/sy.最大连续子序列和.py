n = int(input())
ls = [int(x) for x in input().split()]
dp = [0]*n
start = [0]*n
dp[0] = ls[0]
for i in range(1, n):
    if dp[i-1]>=0:
        dp[i] = dp[i-1]+ls[i]
        start[i] = start[i-1]
    else:
        dp[i] = ls[i]
        start[i] = i
max_val = max(dp)
pos = dp.index(max_val)
print(max_val,start[pos],pos)