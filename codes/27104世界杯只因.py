n = int(input())
nums = [int(x) for x in input().split()]
intervals = []
s = 0
e = n-1
for i in range(n):
    a = nums[i]
    if a > 0:
        intervals.append((i-a, i+a))
intervals.sort()
max_r = 0
cnt = 0
for l, r in intervals:
    if l <= s:
        if r >= e:
            cnt += 1
            break
        max_r = max(max_r, r)
    else:
        s = max_r
        cnt += 1
        max_r = r
print(cnt)
