import heapq

def dijkstra():
    heap = []
    visited = [[False] * n for _ in range(m)]
    heapq.heappush(heap, (0, start_x, start_y))
    while heap:
        num, x, y = heapq.heappop(heap)
        visited[x][y] = True
        if x == end_x and y == end_y:
            return num
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] != '#':
                heapq.heappush(heap, (num + abs(int(matrix[nx][ny]) - int(matrix[x][y])), nx, ny))
                continue
    return 'NO'

m, n, p = map(int, input().split())
matrix = [input().split() for _ in range(m)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(p):
    start_x, start_y, end_x, end_y = map(int, input().split())
    if matrix[start_x][start_y] == '#' or matrix[end_x][end_y] == '#':
        print('NO')
        continue
    print(dijkstra())