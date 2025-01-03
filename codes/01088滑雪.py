r, c = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(r)]
directions = [(1, 0), (-1, 0), (0, 1), (0 ,-1)]
ans = 0
dp = [[0] * c for _ in range(r)]

def dfs(x, y):
    max_length = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] < matrix[x][y]:
            if dp[nx][ny] > 0:
                max_length = max(max_length, dp[nx][ny] + 1)
            else:
                max_length = max(max_length, dfs(nx, ny) + 1)
    dp[x][y] = max_length
    return max_length

for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))
print(ans+1)