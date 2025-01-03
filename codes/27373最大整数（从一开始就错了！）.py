m = int(input())
n = int(input())
nums = input().split()

def compare(a, b):
    return str(max(int(a), int(b)))

def max_combination(a, b):
    return compare(a+b, b+a)

dp = [(['*'] +[0] * m) for _ in range(n)]
num1 = nums[0]
for i in range(m+1):
    if i < len(num1):
        dp[0][i] = '*'
    else:
        dp[0][i] = num1

for i in range(1, n):
    length = len(nums[i])
    for j in range(1, length):
        dp[i][j] = dp[i-1][j]
    for j in range(length, m+1):
        if dp[i-1][j-length] == '*':
            if dp[i-1][j] != '*':
                dp[i][j] = compare(dp[i-1][j], nums[i])
            else:
                dp[i][j] = nums[i]
        else:
            if dp[i-1][j] != '*':
                dp[i][j] = compare(dp[i-1][j], max_combination(dp[i-1][j-length], nums[i]))
            else:
                dp[i][j] = compare(nums[i], max_combination(dp[i-1][j-length], nums[i]))
print(dp)
print(dp[n-1][m])
