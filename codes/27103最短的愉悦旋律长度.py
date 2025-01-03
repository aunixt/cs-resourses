n, m = map(int, input().split())
nums = [int(x) for x in input().split()]
s = set()
cnt = 1
for i in nums:
    s.add(i)
    if len(s) == m:
        cnt += 1
        s.clear()
print(cnt)