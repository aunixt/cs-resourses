case = 0
while True:
    case += 1
    p, e, i, d = map(int,input().split())
    if p == e == i == d == -1:
        break
    p, e, i = p % 23, e % 28, i % 33
    for x in range(d+1, d+21253):
        if x % 23 == p and x % 28 == e and x % 33 == i:
            print('Case {}: the next triple peak occurs in {} days.'.format(case, x-d))
            break
