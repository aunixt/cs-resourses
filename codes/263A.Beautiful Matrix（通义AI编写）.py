x = []
found = False  # 添加一个标记变量
for _ in range(5):
    m = list(map(int, input().split()))
    x.append(m)

for i in range(5):
    for j in range(5):
        if x[i][j] == 1:
            found = True
            break
    if found:
        break

print(x)
print(i)
print(j)
n = abs(i-2) + abs(j-2)
print(n)