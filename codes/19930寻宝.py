from collections import deque
directions = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y,matrix,step):
    q = deque()
    inq = set()
    q.append((x,y,step))
    inq.add((x,y))
    while q:
        x,y,step = q.popleft()
        if matrix[x][y] == 1:
            return step
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in inq and matrix[nx][ny] != 2:
                q.append((nx,ny,step+1))
                inq.add((nx,ny))
    return 'NO'
m, n = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(m)]
print(bfs(0,0,matrix,0))