#pylint:skip-file
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x1, y1, x2, y2, matrix, visited, idx, segment):
    global ans
    if segment >= ans:
        return
    if x1 == x2 and y1 == y2:
        ans = min(ans, segment)
        return
    visited[y1][x1] = True
    for i in range(4):
        nx, ny = x1 + dx[i], y1 + dy[i]
        if 0 <= ny < h+2 and 0 <= nx < w+2 and not visited[ny][nx] and matrix[ny][nx] == 0:
            if i != idx:
                dfs(nx, ny, x2, y2, matrix, visited, i, segment+1)
            else:
                dfs(nx, ny, x2, y2, matrix, visited, idx, segment)
    visited[y1][x1] = False

board = 0
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [[0]*(w+2)]
    for _ in range(h):
        s = list(input())
        temp = [0]
        for si in s:
            if si == 'X':
                temp.append(1)
            else:
                temp.append(0)
        temp.append(0)
        matrix.append(temp)
    matrix.append([0]*(w+2))
    board += 1
    print('Board #{}:'.format(board))
    pair = 0
    while True:
        pair += 1
        visited = [[False]*(w+2) for _ in range(h+2)]
        ans = float('inf')
        x1, y1, x2, y2 = map(int,input().split())
        if x1 == x2 == y1 == y2 == 0:
            break
        matrix[y2][x2] = 0
        dfs(x1, y1, x2, y2, matrix, visited, -1, 0)
        if ans != float('inf'):
            print('Pair {}: {} segments.'.format(pair, ans))
        else:
            print('Pair {}: impossible.'.format(pair))
        matrix[y2][x2] = 1
