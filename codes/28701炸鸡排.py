n, k = map(int, input().split())
times = [int(x) for x in input().split()]
times.sort()
s = sum(times)
while True:
    if times[-1] > s/k:
        s -= times.pop()
        k -= 1
    else:
        print('{:.3f}'.format(s/k))
        break