from math import ceil
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = []
for x in range(0, ceil(n/2)):
    ret = 0
    idx = 0
    i, j = x, x
    while 0 <= i < n and 0 <= j < n and not visited[i][j]:
        visited[i][j] = True
        ret += matrix[i][j]
        di, dj = directions[idx]
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < n and not visited[ni][nj]):
            idx += 1
            if idx == 4:
                break
            else:
                di, dj = directions[idx]
                i, j = i + di, j + dj
        else:
            i, j = ni, nj
    ans.append(ret)
print(max(ans))