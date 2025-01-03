t = int(input())
ret = []
for _ in range(t):
    a, b = map(int, input().split())
    if a % b == 0:
        ret.append(0)
    else:
        n = a//b+1
        ret.append(n*b-a)
print('\n'.join(map(str, ret)))
