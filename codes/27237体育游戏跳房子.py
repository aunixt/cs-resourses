from collections import deque
from math import floor
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    q = deque([(0, n, '')])
    inq = {n}
    while q:
        step, loc, method = q.popleft()
        if loc == m:
            break
        if loc*3 not in inq:
            q.append((step+1, loc*3, method+'H'))
            inq.add(loc*3)
        if floor(loc/2) not in inq:
            q.append((step+1, floor(loc/2), method+'O'))
            inq.add(floor(loc/2))
    print(step)
    print(method)