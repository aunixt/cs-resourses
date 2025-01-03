t = int(input())
for _ in range(t):
    ret = []
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    used_b = [0] * n
    sorted_a = sorted(enumerate(a),key=lambda x:x[1])
    sorted_b = sorted(enumerate(b),key=lambda x:x[1])
    for i in range(n):
        for j in range(n):
            if abs(sorted_a[i][1] - sorted_b[j][1]) <= k and used_b[j] == 0:
                ret.append(sorted_b[j][1])
                used_b[j] = 1
                break
    print(ret)