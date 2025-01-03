case = int(input())
for _ in range(case):
    l, n = map(int, input().split())
    locs = [int(x) for x in input().split()]
    min_time = []
    max_time = []
    for loc in locs:
        min_time.append(min(loc, l-loc))
        max_time.append(max(loc, l-loc))
    print(max(min_time), max(max_time))