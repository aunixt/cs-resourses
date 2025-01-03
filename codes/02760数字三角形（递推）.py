N = int(input())
tri = []
for _ in range(N):
    tri.append([int(x) for x in input().split()])
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[N-1][i] = tri[N-1][i]
for i in range(N-2,-1,-1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + tri[i][j]
print(dp[0][0])