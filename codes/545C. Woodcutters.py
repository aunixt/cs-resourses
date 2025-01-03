n = int(input())
loc = []
height = []
ans = 2

for _ in range(n):
    x, h = map(int, input().split())
    loc.append(x)
    height.append(h)

k = loc[0]
for i in range(1, n-1):
    if loc[i] - k - 1 >= height[i]:
        ans += 1
        k = loc[i]
    else:
        if loc[i+1] - loc[i] - 1 >= height[i]:
            ans += 1
            k = loc[i] + height[i]
        else:
            k = loc[i]
if n == 1:
    ans = 1
print(ans)