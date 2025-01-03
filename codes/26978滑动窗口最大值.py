from collections import deque, defaultdict
import heapq

n, k = map(int, input().split())
nums = [int(x) for x in input().split()]
window = deque(nums[0:k])
heap = [-x for x in nums[0:k]]
heapq.heapify(heap)
out = defaultdict(int)
ans = []
a = heapq.heappop(heap)
ans.append(-a)
heapq.heappush(heap, a)
for i in range(k,n):
    out[window.popleft()] += 1
    window.append(nums[i])
    heapq.heappush(heap, -nums[i])
    a = heapq.heappop(heap)
    while out[-a]:
        out[-a] -= 1
        a = heapq.heappop(heap)
    heapq.heappush(heap, a)
    ans.append(-a)
print(*ans)