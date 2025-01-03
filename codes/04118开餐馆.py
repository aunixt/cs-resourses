t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    locations = [int(x) for x in input().split()]
    profits = [int(x) for x in input().split()]
    dp = profits[:]
    for i in range(n):
        for j in range(i):
            if locations[i] - locations[j] > k:
                dp[i] = max(dp[i], dp[j] + profits[i])
    print(max(dp))