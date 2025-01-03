from math import sqrt
A = int(input())
ls = [int(x) for x in str(A)]
def dfs(i):
    if i == len(ls):
        return True
    num = 0
    for j in range(i,len(ls)):
        num = num * 10 + ls[j]
        if sqrt(num) % 1 == 0 and num != 0:
            if dfs(j+1):
                return True
    return False
print('Yes' if dfs(0) else 'No')