import sys
sys.setrecursionlimit(300000)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, height, water_height):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < height:
            if water_height[nx][ny] < height:
                water_height[nx][ny] = height
                dfs(nx, ny, height, water_height)

ans = []
data = sys.stdin.read().split()
idx = 0
k = int(data[idx])
idx += 1
for _ in range(k):
    m, n = map(int, data[idx:idx + 2])
    idx += 2
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, data[idx:idx + n])))
        idx += n
    i, j = map(int, data[idx:idx + 2])
    idx += 2
    i, j = i - 1, j - 1
    p = int(data[idx])
    idx += 1
    water_height = [[0] * n for _ in range(m)]
    for _ in range(p):
        x, y = map(int, data[idx:idx + 2])
        idx += 2
        x, y = x - 1, y - 1
        if matrix[x][y] < matrix[i][j]:
            continue
        dfs(x, y, matrix[x][y], water_height)
    ans.append('Yes' if water_height[i][j] > 0 else 'No')
sys.stdout.write('\n'.join(ans) + '\n')