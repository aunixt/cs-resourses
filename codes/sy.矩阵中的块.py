from collections import deque
directions = [(1,0),(-1,0),(0,1),(0,-1)]
inq = set()
q = deque()
cnt = 0
def bfs(x,y,inq,q,directions,matrix):
    inq.add((x,y))
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if (nx,ny) not in inq and matrix[nx][ny] == 1:
                inq.add((nx,ny))
                q.append((nx,ny))
n, m = map(int, input().split())
matrix = [[-1]*(m+2)] + [([-1] + [int(x) for x in input().split()] + [-1]) for _ in range(n)] + [[-1]*(m+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j] == 1 and (i,j) not in inq:
            bfs(i,j,inq,q,directions,matrix)
            cnt += 1
print(cnt)