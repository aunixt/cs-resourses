directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
def dfs(x,y):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        if matrix[x][y] != 'W':
            continue
        matrix[x][y] = '.'
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] == 'W':
                stack.append((nx, ny))
n, m = map(int, input().split())
cnt = 0
matrix = []
matrix.append([0]*(m+2))
for _ in range(n):
    matrix.append([0]+list(input())+[0])
matrix.append([0]*(m+2))
for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j] == 'W':
            dfs(i,j)
            cnt += 1
print(cnt)


