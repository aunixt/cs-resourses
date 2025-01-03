ans = []
intervals = eval(input())
intervals.sort()
end = intervals[0][1]
start = intervals[0][0]
for interval in intervals[1:]:
    s, e = interval[0], interval[1]
    if s <= end:
        end = max(end, e)
    else:
        ans.append([start, end])
        start = s
        end = e
ans.append([start, end])
print(ans)