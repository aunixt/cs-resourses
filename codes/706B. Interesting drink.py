from bisect import bisect_right
n = int(input())
prices = [int(x) for x in input().split()]
prices.sort()
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect_right(prices,m))