def min_money(values,weights,total_weight):
    dp = [float('inf')] * (total_weight + 1)
    dp[0] = 0
    for i in range(len(values)):
        for j in range(weights[i], total_weight + 1):
            dp[j] = min(dp[j], dp[j-weights[i]] + values[i])
    return dp[-1]

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    total_weight = b - a
    values = []
    weights = []
    N = int(input())
    for _ in range(N):
        v,w = map(int,input().split())
        values.append(v)
        weights.append(w)
    ans = min_money(values,weights,total_weight)
    if ans == float('inf'):
        print('This is impossible.')
    else:
        print('The minimum amount of money in the piggy-bank is {}.'.format(ans))