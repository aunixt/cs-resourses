from math import sqrt

def num_of_radar(length,d,loc):
    ls = []
    for i in range(length):
        x, y = loc[i]
        rg = [x-sqrt(d**2-y**2),x+sqrt(d**2-y**2)]
        ls.append(rg)
    ls.sort(key=lambda x: x[0])
    combined_ls = []
    combined_range = [ls[0][0]]
    right = ls[0][1]
    for i in range(1,len(ls)):
        if ls[i][0] > right:
            combined_range.append(right)
            combined_ls.append(combined_range)
            combined_range = [ls[i][0]]
            right = ls[i][1]
            continue
        else:
            right = max(right,ls[i][1])
    combined_range.append(right)
    combined_ls.append(combined_range)
    return len(combined_ls)

case = 1
loc = []
while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    for _ in range(n+1):
        rg = list(map(int, input().split()))
        if not rg:
            print('Case {}: {}'.format(case, num_of_radar(len(loc),d,loc)))
            case += 1
            loc = []
            continue
        else:
            loc.append(rg)