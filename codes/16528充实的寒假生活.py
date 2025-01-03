n = int(input())
intervals = [[int(x) for x in input().split()] for _ in range(n)]
intervals.sort(key=lambda x: x[1])
end = -float('inf')
ans = 0
for i in range(n):
    a, b = intervals[i]
    if a > end:
        ans += 1
        end = b
print(ans)