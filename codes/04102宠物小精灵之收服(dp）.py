n, m, k = map(int, input().split())
dp = [[-1]* (m+1) for _ in range(k+1)]
dp[0][m] = n
for i in range(k):
    ball, cost = map(int, input().split())
    for y in range(m):
        for x in range(i+1, 0, -1):
            if y + cost <= m and dp[x-1][y+cost] != -1:
                dp[x][y] = max(dp[x][y], dp[x-1][y+cost] - ball)
def find():
    for i in range(k, -1, -1):
        for j in range(m, -1, -1):
            if dp[i][j] != -1:
                print(i, j)
                return
find()