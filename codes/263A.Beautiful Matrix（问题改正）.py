x = []
for _ in range(5):
    m = list(map(int, input().split()))
    x.append(m)
for i in range(5):
    for j in range(5):
        if x[i][j] == 1:
            break
    else:
        continue #内层循环没有找到规定的数值，则继续进行循环（不执行第十一行的break）
    break #找到‘1’之后，退出外层循环
n = abs(i-2) + abs(j-2)
print(n)