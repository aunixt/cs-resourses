import heapq
from collections import defaultdict
stack = []
weight = []
deleted = defaultdict(int)
while True:
    try:
        s = input().split()
        if s[0] == 'pop':
            if stack:
                deleted[stack.pop()] += 1
        elif s[0] == 'min':
            if stack:
                while True:
                    x = heapq.heappop(weight)
                    if not deleted[x]:
                        heapq.heappush(weight, x)
                        print(x)
                        break
                    deleted[x] -= 1
        else:
            n = int(s[1])
            stack.append(n)
            heapq.heappush(weight, n)
    except EOFError:
        break