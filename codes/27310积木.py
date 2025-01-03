n = int(input())
bricks = [set(input()) for _ in range(4)]
ans = []
def dfs(target, idx, used):
    if k == len(ans)-1:
        return
    if idx == len(target):
        ans.append('YES')
        return
    letter = target[idx]
    for i in range(4):
        if not used[i] and letter in bricks[i]:
            used[i] = True
            dfs(target, idx+1, used)
            used[i] = False

for k in range(n):
    dfs(input(), 0, [False]*4)
    if k > len(ans)-1:
        ans.append('NO')

for i in range(n):
    print(ans[i])