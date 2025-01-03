import math

n = 1000000
pr = []
nprime = [True]*n
for i in range(2,n+1):
    if nprime[i-1]:
        pr.append(i)
    for p in pr:
        if p*i > n:
            break
        nprime[p*i-1] = False
        if i % p == 0:
            break
pr = set(pr)
n = int(input())
ls = list(map(int,input().split()))
for i in ls:
    x = math.sqrt(i)
    if i <= 3:
        print('NO')
        continue
    elif x % 1 != 0:
        print('NO')
        continue
    else:
       if x in pr:
           print('YES')
       else:
           print('NO')