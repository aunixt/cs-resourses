prices = [int(x) for x in input().split()]
n = len(prices)
dp = [0]*n
minimum_price = prices[0]
for i in range(1, n):
    if prices[i] < minimum_price:
        minimum_price = prices[i]
    else:
        dp[i] = prices[i] - minimum_price
print(max(dp))