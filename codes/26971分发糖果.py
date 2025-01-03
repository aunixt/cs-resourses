n = int(input())
nums = [int(x) for x in input().split()]
ans = 0

left = [0] * n
left[0] = 1
for i in range(1, n):
    if nums[i] > nums[i-1]:
        left[i] = left[i-1] + 1
    else:
        left[i] = 1

right = 1
ans += max(right, left[n-1])
for i in range(n-2, -1, -1):
    if nums[i] > nums[i+1]:
        right += 1
    else:
        right = 1
    ans += max(left[i], right)

print(ans)