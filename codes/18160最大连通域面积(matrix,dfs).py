directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def dfs(x, y, matrix, visited):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    while stack:
        x, y = stack.pop()
        area += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] == 'W' and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
    return area

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [[0]*(m+2)]
    for _ in range(n):
        matrix.append([0] + list(input()) + [0])
    matrix.append([0]*(m+2))
    visited = [[False] * (m+2) for _ in range(n+2)]
    max_area = 0
    for x in range(1,n+1):
        for y in range(1,m+1):
            if matrix[x][y] == 'W' and not visited[x][y]:
                max_area = max(max_area, dfs(x, y, matrix, visited))
    print(max_area)
