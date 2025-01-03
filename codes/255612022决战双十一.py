n, m = map(int, input().split())
prices = [input().split() for _ in range(n)]
coupons = [input().split() for _ in range(m)]
ans = float('inf')
store_prices = [0] * m

def dfs(item):
    global ans
    if item == n:
        total_coupon = 0
        for i in range(m):
            store_coupon = 0
            store_price = store_prices[i]
            for coupon in coupons[i]:
                a, b = map(int, coupon.split('-'))
                if store_price >= a:
                    store_coupon = max(store_coupon, b)
            total_coupon += store_coupon
        total_price = sum(store_prices) - total_coupon - sum(store_prices) // 300 * 50
        ans = min(ans, total_price)
        return
    for price in prices[item]:
        idx, p = map(int, price.split(':'))
        store_prices[idx-1] += p
        dfs(item+1)
        store_prices[idx-1] -= p

dfs(0)
print(ans)