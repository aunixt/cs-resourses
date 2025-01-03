from functools import lru_cache

n, m, k = map(int, input().split())
balls = []
cost = []
health = 0
ans = 0
for _ in range(k):
    a, b = map(int, input().split())
    balls.append(a)
    cost.append(b)

@lru_cache()
def dfs(left_ball, left_health, cnt, idx):
    global ans, health

    if idx == k or left_ball < 0 or left_health < 0:
        left_ball += balls[idx-1]
        left_health += cost[idx-1]
        cnt -= 1
        if cnt > ans:
            ans = cnt
            health = left_health
            return
        elif cnt == ans:
            if left_health > health:
                health = left_health
                return
        return

    dfs(left_ball - balls[idx], left_health - cost[idx], cnt + 1, idx + 1)
    dfs(left_ball, left_health, cnt, idx + 1)

dfs(n, m, 0, 0)
print(ans, health)