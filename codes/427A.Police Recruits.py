n = int(input())
nums = list(map(int,input().split()))
untreated_crimes_mun = 0
officers = 0
for i in nums:
    if i < 0 and officers == 0:
        untreated_crimes_mun += 1
        continue
    if i > 0:
        officers += i
        continue
    officers -= 1
print(untreated_crimes_mun)