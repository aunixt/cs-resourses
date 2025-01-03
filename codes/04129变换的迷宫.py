from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(start_x, start_y):
    q = deque([(0, start_x, start_y)])
    inq = {(0, start_x, start_y)}
    while q:
        step, x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            condition = (step+1) % k
            if 0 <= nx < r and 0 <= ny < c and (condition, nx, ny) not in inq:
                if matrix[nx][ny] == 'E':
                    return step + 1
                if condition == 0 or matrix[nx][ny] != '#':
                    q.append((step+1, nx, ny))
                    inq.add((condition, nx, ny))
    return 'Oop!'

t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    matrix = [list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'S':
                print(bfs(i, j))