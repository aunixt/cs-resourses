#pylint:skip-file
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x1, y1, x2, y2):
    global ans
    q = deque([(y1, x1, 0, -1)])
    inq = {(y1, x1)}
    while q:
        y, x, segment, idx = q.popleft()
        if y == y2 and x == x2:
            ans = min(ans, segment)
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < h+2 and 0 <= nx < w+2 and (ny, nx) not in inq and matrix[ny][nx] == 0:
                if i != idx:
                    q.append((ny, nx, segment + 1, i))
                    inq.add((ny, nx))
                else:
                    q.append((ny, nx, segment, idx))
                    inq.add((ny, nx))

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
        ans = float('inf')
        x1, y1, x2, y2 = map(int,input().split())
        if x1 == x2 == y1 == y2 == 0:
            break
        matrix[y2][x2] = 0
        bfs(x1, y1, x2, y2)
        if ans != float('inf'):
            print('Pair {}: {} segments.'.format(pair, ans))
        else:
            print('Pair {}: impossible.'.format(pair))
        matrix[y2][x2] = 1
    print()