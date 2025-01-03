L, n, m = map(int, input().split())
positions = [0]
for _ in range(n):
    positions.append(int(input()))
positions.append(L)

def the_num_of_removed_rocks(mid):
    current_position = 0
    cnt = 0
    for i in range(1, n+2):
        if positions[i] - current_position >= mid:
            current_position = positions[i]
        else:
            cnt += 1
    return cnt

#针对最短跳跃距离二分
l = 0
r = L
ans = 0
while l <= r:
    mid = (l+r)//2
    if the_num_of_removed_rocks(mid) > m:
        r = mid-1
    elif the_num_of_removed_rocks(mid) == m:
        ans = mid
        l = mid+1
    elif the_num_of_removed_rocks(mid) < m:
        l = mid+1

print(ans)