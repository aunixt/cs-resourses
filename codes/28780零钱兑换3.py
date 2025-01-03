def make_changes(dp,coins,change):
    for cents in range(1,change+1):
        for coin in coins:
            if cents >= coin:
                dp[cents] = min(dp[cents],dp[cents-coin]+1)
    return dp[-1] if dp[-1] != float("inf") else -1
n,m = map(int,input().split())
coins = [int(x) for x in input().split()]
dp = [float('inf')]*(m+1)
dp[0] = 0
print(make_changes(dp,coins,m))