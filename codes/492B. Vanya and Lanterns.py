n, l = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = [nums[0], l - nums[-1]]
for i in range(1, n):
    ans.append((nums[i] - nums[i-1])/2)
print(max(ans))