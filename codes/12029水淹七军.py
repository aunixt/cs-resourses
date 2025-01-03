import sys
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start_x, start_y, water_height):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if matrix[nx][ny] <= water_height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


ans = []
input = sys.stdin.read
data = input().split()
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
    water_points = []
    for _ in range(p):
        x, y = map(int, data[idx:idx + 2])
        idx += 2
        water_points.append((x - 1, y - 1))

    visited = [[False] * n for _ in range(m)]

    for x, y in water_points:
        if not visited[x][y]:
            bfs(x, y, matrix[x][y])

    ans.append("Yes" if visited[i][j] else "No")

sys.stdout.write("\n".join(ans) + "\n")
