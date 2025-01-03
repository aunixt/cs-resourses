from math import sqrt

def num_of_radar(d,loc):
    ls = []
    for i in range(len(loc)):
        x, y = loc[i]
        if y > d:
            return -1
        ls.append([x-sqrt(d**2-y**2),x+sqrt(d**2-y**2)])
    ls.sort(key=lambda x: x[1])
    ans = 0
    ed = -float('inf')
    for v in ls:
        if ed < v[0]:
            ans += 1
            ed = v[1]
    return ans

case = 1
loc = []
while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    for _ in range(n+1):
        rg = list(map(int, input().split()))
        if not rg:
            print('Case {}: {}'.format(case, num_of_radar(d,loc)))
            case += 1
            loc = []
            continue
        else:
            loc.append(rg)