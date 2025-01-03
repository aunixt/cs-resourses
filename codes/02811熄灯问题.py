import copy
matrix = [[int(x) for x in input().split()] for _ in range(5)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def press(temp):
    grid = copy.deepcopy(matrix)

    def calculate(temp, i):
        for j in range(6):
            if temp[j] == 1:
                grid[i][j] = grid[i][j] ^ 1
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < 5 and 0 <= ny < 6:
                        grid[nx][ny] = grid[nx][ny] ^ 1

    ans = [temp]
    calculate(temp, 0)
    for i in range(4):
        temp = grid[i]
        ans.append(temp[:])
        calculate(temp, i+1)
    if grid[4] == [0]*6:
        for x in ans:
            print(*x)

def permutation(temp):
    if len(temp) == 6:
        press(temp)
        return
    permutation(temp + [0])
    permutation(temp + [1])

permutation([])

