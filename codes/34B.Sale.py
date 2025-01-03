n, m = map(int, input().split())
prices = list(map(int,input().split()))
prices.sort()
minus_price_num = 0
earning = 0
for i in range(n):
    if prices[i] < 0:
        minus_price_num += 1
    else:
        break
if minus_price_num <= m:
    for i in range(minus_price_num):
        earning += prices[i]
else:
    for i in range(m):
        earning += prices[i]
print(earning * (-1))

