text1 = input()
text2 = input()
m = len(text1)
n = len(text2)
dp = [[0] * n for _ in range(m)]

idx1 = text1.find(text2[0])
if idx1 >= 0:
    for i in range(idx1, m):
        dp[i][0] = 1
idx2 = text2.find(text1[0])
if idx2 >= 0:
    for j in range(idx2, n):
        dp[0][j] = 1

for i in range(1, m):
    for j in range(1, n):
        if text1[i] == text2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m-1][n-1])