n, a, b, c = map(int,input().split())
dp = [0] + [-float('inf')]*4000
for i in range(1,n+1):  #i为对应长度的ribbon
    dp[i] = max(dp[i-a],dp[i-b],dp[i-c]) + 1    #局部最优
print(dp[n])