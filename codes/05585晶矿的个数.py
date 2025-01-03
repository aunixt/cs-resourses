directions = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,type,n):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        matrix[x][y] = '#'
        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == type:
                stack.append((nx,ny))
k = int(input())
for _ in range(k):
    n = int(input())
    num_of_r, num_of_b = 0, 0
    matrix = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'r':
                dfs(i,j,'r',n)
                num_of_r += 1
            elif matrix[i][j] == 'b':
                dfs(i,j,'b',n)
                num_of_b += 1
    print(num_of_r, num_of_b)