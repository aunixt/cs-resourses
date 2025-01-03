from math import ceil
while True:
    n = int(input())
    if n == 0:
        break
    time = float('inf')
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        arrival_time = (4.5 / v) * 3600 + t
        if arrival_time < time:
            time = arrival_time
    print(ceil(time))