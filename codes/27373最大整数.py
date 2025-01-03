m = int(input())
n = int(input())
nums = input().split()

def translate_to_int(a):
    if a == '':
        return 0
    else:
        return int(a)

#冒泡排序，使得任意前后两个数字顺序相加后均大于逆序相加
for i in range(n):
    for j in range(n-i-1):
        if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

dp = [[''] * (m+1) for _ in range(n)]
num1 = nums[0]
for i in range(m+1):
    if i >= len(num1):
        dp[0][i] = num1

for i in range(1, n):
    length = len(nums[i])
    for j in range(1, m+1):
        if j < length:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = str(max(translate_to_int(dp[i-1][j]), int(dp[i-1][j-length] + nums[i])))

print(dp[n-1][m])