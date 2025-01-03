from collections import deque
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(x, y):
    matrix[x][y] = 2
    q.append((x, y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] == 1:
                dfs(nx, ny)

def bfs():
    inq = set(q)
    step = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in inq:
                    if matrix[nx][ny] == 0:
                        q.append((nx, ny))
                        inq.add((nx, ny))
                    elif matrix[nx][ny] == 1:
                        return step
        step += 1

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
q = deque()

def main():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                dfs(i, j)
                return bfs()

print(main())
