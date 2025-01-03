d = int(input())
n = int(input())
matrix = [[0] * 1025 for _ in range(1025)]
for _ in range(n):
    x, y, i = map(int,input().split())
    for a in range(max(0,x-d),min(1025,x+d+1)):
        for b in range(max(0,y-d),min(1025,y+d+1)):
            matrix[a][b] += i
max_trash = 0
cnt = 0
for i in range(1025):
    for j in range(1025):
        if matrix[i][j] > max_trash:
            cnt = 1
            max_trash = matrix[i][j]
        elif matrix[i][j] == max_trash:
            cnt += 1
print(cnt,max_trash)