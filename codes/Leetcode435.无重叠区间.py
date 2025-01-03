intervals = eval(input())
cnt = 0
intervals.sort(key = lambda x: x[1])
end = intervals[0][1]
for interval in intervals[1:]:
    s, e = interval[0], interval[1]
    if s < end:
        cnt += 1
        continue
    else:
        end = e
print(cnt)