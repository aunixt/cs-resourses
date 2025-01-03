while True:
    n = int(input())
    if n == 0:
        break
    t_horses = [int(x) for x in input().split()]
    k_horses = [int(x) for x in input().split()]
    t_horses.sort(reverse=True)
    k_horses.sort(reverse=True)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if t_horses[i-1] > k_horses[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            elif t_horses[i-1] < k_horses[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    print(dp[n][n]*200)