import heapq

n = int(input())
potions = [int(x) for x in input().split()]
health = 0
cnt = 0
consumed_negative_potions = []
for potion in potions:
    health += potion
    cnt += 1
    if potion < 0:
        heapq.heappush(consumed_negative_potions, potion)
    while health < 0 and consumed_negative_potions:
        health -= heapq.heappop(consumed_negative_potions)
        cnt -= 1
print(cnt)
