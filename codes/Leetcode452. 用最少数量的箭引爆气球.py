points = eval(input())
points.sort(key = lambda x:x[1])
cnt = 1
end = points[0][1]
for point in points:
    s, e = point[0], point[1]
    if s <= end:
        continue
    else:
        end = e
        cnt += 1
print(cnt)