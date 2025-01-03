n, c = map(int, input().split())
stalls = []
for _ in range(n):
    stalls.append(int(input()))
stalls.sort()
lower_limit = 0
upper_limit = (stalls[-1] - stalls[0]) // (c-1)
while lower_limit <= upper_limit:
    mid = (lower_limit + upper_limit) // 2
    current_location = stalls[0]
    cnt = 1
    for i in range(1, n):
        if stalls[i] - current_location >= mid:
            cnt += 1
            current_location = stalls[i]
    if cnt >= c:
        lower_limit = mid + 1
    else:
        upper_limit = mid - 1
print(upper_limit)