n = int(input())
x_coordinate = 0
y_coordinate = 0
z_coordinate = 0
for _ in range(n):
    x, y, z = map(int, input().split())
    x_coordinate += x
    y_coordinate += y
    z_coordinate += z
if x_coordinate == 0 and y_coordinate == 0 and z_coordinate == 0:
    print('YES')
else:
    print('NO')