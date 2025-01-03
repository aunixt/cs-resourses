from collections import deque
n = int(input())
def bfs(n):
    q = deque()
    inq = set()
    q.append((1,0))
    inq.add(1)
    while q:
        num, step = q.popleft()
        if num == n:
            return step

        if num+1 <= n and num+1 not in inq:
            inq.add(num+1)
            q.append((num+1,step+1))
        if num*2 <= n and num*2 not in inq:
            inq.add(num*2)
            q.append((num*2,step+1))
print(bfs(n))