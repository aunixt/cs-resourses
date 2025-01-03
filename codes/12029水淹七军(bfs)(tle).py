import sys
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, total_height):
    q = deque([(i, j)])
    inq = set()
    inq.add((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] <= total_height and (nx, ny) not in inq:
                matrix[nx][ny] = total_height
                q.append((nx, ny))
                inq.add((nx, ny))

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
    boss_height = matrix[i][j]
    p = int(data[idx])
    idx += 1
    for _ in range(p):
        x, y = map(int, data[idx:idx + 2])
        idx += 2
        x, y = x - 1, y - 1
        if matrix[x][y] < boss_height:
            continue
        bfs(x, y, matrix[x][y])
    ans.append('Yes' if matrix[i][j] > boss_height else 'No')
sys.stdout.write('\n'.join(ans) + '\n')