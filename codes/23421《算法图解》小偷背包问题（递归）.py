def max_v(i,left_weight):
    if left_weight < 0:
        return -float('inf')
    if i == N:
        return 0
    return max(max_v(i+1,left_weight),v[i] + max_v(i+1,left_weight-w[i]))

N, B = map(int, input().split())
v = list(map(int, input().split()))
w = list(map(int, input().split()))
print(max_v(0,B))