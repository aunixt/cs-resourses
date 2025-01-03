n = int(input())
a, b = map(int, input().split())
nums = [[int(x) for x in input().split()] for _ in range(n)]
nums.sort(key = lambda x: (x[0] * x[1]))
ans = 0
for i in range(n):
    ans = max(ans, a // nums[i][1])
    a *= nums[i][0]
print(ans)