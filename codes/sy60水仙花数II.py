a, b = map(int, input().split())
s = []
for n in range(a, b+1):
    str_n = str(n)
    x, y, z = map(int, list(str_n))
    if x**3+y**3+z**3==n:
        s.append(n)
if len(s) > 0:
    print(*s)
else:
    print('NO')
