n = int(input())
nums = [int(x) for x in input().split()]
sorted_nums = sorted(nums)
dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)
for i in range(1, n + 1):
    dp1[i] = dp1[i - 1] + nums[i - 1]
    dp2[i] = dp2[i - 1] + sorted_nums[i - 1]
m = int(input())
for _ in range(m):
    tp, l, r = map(int, input().split())
    if tp == 1:
        print(dp1[r] - dp1[l-1])
    if tp == 2:
        print(dp2[r] - dp2[l-1])