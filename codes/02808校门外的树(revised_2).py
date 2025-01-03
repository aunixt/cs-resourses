l, m = map(int, input().split())
r = [(0, l)]
left = 0
for _ in range(m):
    a, b = map(int, input().split())
    new_r = []
    for start, end in r:
        if a <= end and b >= start:
            if a > start:
                new_r.append((start, a - 1))
            if b < end:
                new_r.append((b + 1, end))
        else:
            new_r.append((start, end))
    r = new_r
for start, end in r:
    left += end - start + 1
print(left)