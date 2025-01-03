N,B = map(int,input().split())
values = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
dp = [0]*(B+1)
for i in range(N):
    for j in range(B,weights[i]-1,-1):
        dp[j] = max(dp[j],dp[j-weights[i]]+values[i])
print(dp[-1])