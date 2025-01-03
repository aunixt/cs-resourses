#pylint:skip-file
T = int(input())
directions = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def dfs(x, y, step):
    global cnt
    visited[x][y] = True
    if step == n*m-1:
        cnt += 1
        visited[x][y] = False
        return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx, ny, step+1)
    visited[x][y] = False

for _ in range(T):
    n, m, x, y = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    dfs(x, y, 0)
    print(cnt)