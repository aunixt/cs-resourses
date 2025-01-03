l, m = map(int, input().split())
r = [(0, l)]
left = 0
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(len(r)):
        if r[i][0] < a < r[i][1] and r[i][0] < b < r[i][1]:
            r.insert(i+1, (b+1, r[i][1]))
            r[i] = (r[i][0], a-1)
            break
        elif r[i][0] == a and r[i][1] == b:
            break
        elif r[i][0] == a and r[i][0] < b < r[i][1]:
            r[i] = (a, b+1)
            break
        elif r[i][1] == b and r[i][0] < a < r[i][1]:
            r[i] = (a-1, b)
            break
        elif r[i][0] <= a <= r[i][1] and not r[i][0] <= b <= r[i][1]:
            r[i] = (r[i][0], a-1)
            for j in range(i,len(r)):
                if r[j][0] <= b <= r[j][1]:
                    r[j] = (b+1, r[j][1])
                    break
for k in range(len(r)):
    left += r[k][1] - r[k][0] + 1
print(left)