import heapq

def dijkstra():

    heap = []
    heapq.heappush(heap, (0, start_x, start_y))
    min_cost = [[float('inf')] * n for _ in range(m)]
    min_cost[start_x][start_y] = 0

    while heap:
        num, x, y = heapq.heappop(heap)

        if num > min_cost[x][y]:
            continue

        if x == end_x and y == end_y:
            return num

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                cost = num + abs(int(matrix[nx][ny]) - int(matrix[x][y]))
                if cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))

    return 'NO'

m, n, p = map(int, input().split())
matrix = [input().split() for _ in range(m)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(p):
    start_x, start_y, end_x, end_y = map(int, input().split())
    if matrix[start_x][start_y] == '#' or matrix[end_x][end_y] == '#':
        print('NO')
    else:
        print(dijkstra())
