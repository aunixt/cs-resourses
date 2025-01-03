A, B, C = [], [], []

a, b = map(int, input().split())
for i in range(a):
    A.append([int(x) for x in input().split()])

c, d = map(int, input().split())
for i in range(c):
    B.append([int(x) for x in input().split()])

e, f = map(int, input().split())
for i in range(e):
    C.append([int(x) for x in input().split()])

if a!=e or d!=f or b!=c :
    print('Error!')
else:
    for i in range(e):
        for j in range(f):
            C[i][j] += sum(A[i][k]*B[k][j] for k in range(b))
    for i in range(e):
        print(*C[i])