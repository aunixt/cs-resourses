from collections import deque
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def find_start():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 5:
                return i, j
s_x, s_y = find_start()

def find_other():
    for dx, dy in directions:
        nx, ny = s_x + dx, s_y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 5:
            o_x, o_y = nx, ny
            return o_x, o_y
o_x, o_y = find_other()
d_o_x, d_o_y = o_x - s_x, o_y - s_y

def bfs():
    q = deque([(s_x, s_y)])
    inq = {(s_x, s_y)}
    while q:
        x, y = q.popleft()
        if matrix[x][y] == 9 or matrix[x + d_o_x][y + d_o_y] == 9:
            return 'yes'
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in inq:
                if 0 <= nx + d_o_x < n and 0 <= ny + d_o_y < n:
                    if matrix[nx][ny] != 1 and matrix[nx + d_o_x][ny + d_o_y] != 1:
                        q.append((nx, ny))
                        inq.add((nx, ny))
    return 'no'

print(bfs())