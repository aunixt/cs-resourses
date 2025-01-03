while True:
    try:
        n = int(input())
    except EOFError:
        break
    dp = [[0] * (n+1) for _ in range(n+1)]
    for x in range(1, n+1):
        dp[x][0] = 1
        dp[x][1] = 1
    for x in range(2, n+1):
        dp[1][x] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j - i >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-i]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][n])