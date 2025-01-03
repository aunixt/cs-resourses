directions = [(0,1),(1,0)]
def dfs(x,y):
    stack = [(x,y)]
    while stack:
        x, y = stack.pop()
        matrix[x][y] = 1
        if x == n-1 and y == n-1:
            return 'Yes'
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
                stack.append((nx, ny))
    return 'No'
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
print(dfs(0,0))
