n,m = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(n)]
directions = [(-1,0),(1,0),(0,1),(0,-1)]
cnt = 0
for x in range(n):
    for y in range(m):
        if mp[x][y] == 1:
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or mp[nx][ny] == 0:
                    cnt += 1
print(cnt)