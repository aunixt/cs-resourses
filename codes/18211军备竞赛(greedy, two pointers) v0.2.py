p = int(input())
ls = list(map(int,input().split()))
ls.sort()
more_weapons = 0
ans = 0
n = len(ls)
i, j = 0, n-1
while i <= j:
    if ls[i] <= p:
        more_weapons += 1
        ans = max(ans, more_weapons)
        p -= ls[i]
        i += 1
    else:
        more_weapons -= 1
        if more_weapons < 0:
            ans = 0
            break
        p += ls[j]
        j -= 1
print(ans)