n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
path = []
max_sum = -float('inf')
visited = [[False] * m for _ in range(n)]

def dfs(x, y, temp, now_sum):
    global max_sum, path
    visited[x][y] = True
    temp.append((x,y))
    now_sum += matrix[x][y]
    if x == n-1 and y == m-1:
        if now_sum > max_sum:
            max_sum = now_sum
            path = temp[:]
            temp.pop()
            visited[x][y] = False
            return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx, ny, temp, now_sum)
    temp.pop()
    visited[x][y] = False
dfs(0, 0 ,[], 0)
for x, y in path:
    print(x+1, y+1)