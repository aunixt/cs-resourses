n, a, b = map(int, input().split())
nums = [int(x) for x in input().split()]
i = 0
j = n-1
left_a = a
left_b = b
cnt = 0
while i < j:
    if left_a < nums[i]:
        cnt += 1
        left_a = a
    if left_b < nums[j]:
        cnt += 1
        left_b = b
    left_a -= nums[i]
    left_b -= nums[j]
    i += 1
    j -= 1
if i == j:
    if max(left_a, left_b) < nums[i]:
        cnt += 1
print(cnt)
