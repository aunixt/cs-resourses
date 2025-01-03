prices = [int(x) for x in input().split(',')]
n = len(prices)
dp1 = [0] * n
dp2 = [0] * n
dp1[0] = prices[0]
dp2[0] = prices[0]
for i in range(1, n):
    dp1[i] = max(dp1[i-1] + prices[i], prices[i])
    dp2[i] = max(dp1[i-1], dp2[i-1] + prices[i], prices[i])
print(max(dp2))

