class Solution:
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        d_idx = 0
        order = []
        x, y = 0, 0
        for i in range(row*col):
            order.append(matrix[x][y])
            matrix[x][y] = '*'
            dx, dy = directions[d_idx]
            if not (0 <= x + dx < row and 0 <= y + dy < col and matrix[x + dx][y + dy] != '*'):
                d_idx = (d_idx + 1) % 4
            x += directions[d_idx][0]
            y += directions[d_idx][1]
        return order
matrix = eval(input())
x = Solution().spiralOrder(matrix)
print(x)

