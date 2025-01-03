memo = {}
def L(heights,i):
    if i in memo:
        return memo[i]

    if i == k - 1:
        return 1

    max_len = 1
    for j in range(i+1,len(heights)):
        if heights[j] <= heights[i]:
            max_len = max(max_len,L(heights,j)+1)

    memo[i] = max_len
    return max_len

k = int(input())
heights = list(map(int,input().split()))
ret = [L(heights,i) for i in range(k)]
print(max(ret))