while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    t_horses = [int(x) for x in input().split()]
    k_horses = [int(x) for x in input().split()]
    t_horses.sort()
    k_horses.sort()
    lt, rt = 0, n-1
    lk, rk = 0, n-1
    while lt <= rt:
        if t_horses[rt] > k_horses[rk]:
            cnt += 1
            rt -= 1
            rk -= 1
        elif t_horses[lt] > k_horses[lk]:
            cnt += 1
            lt += 1
            lk += 1
        else:
            if t_horses[lt] < k_horses[rk]:
                cnt -= 1
            lt += 1
            rk -=1
    print(cnt * 200)