n, t = map(int, input().split())
prices = [int(x) for x in input().split()]
sum_price = sum(prices)
dp = [0]*(sum_price+1)
for i in range(n):
    price = prices[i]
    for j in range(sum_price, price, -1):
        if dp[j-price] > 0:
            dp[j] = dp[j-price] + prices[i]
    dp[price] = price

def main():
    for i in range(t, sum_price+1):
        if dp[i] > 0:
            return dp[i]
    return 0

print(main())
