from math import ceil
while True:
    n = int(input())
    v_and_t = {}
    current_v = 0
    start_t = 0
    s = 0

    if n == 0:
        break

    for _ in range(n):
        a, b = map(int,input().split())
        v_and_t[a] = b
    v_and_t = sorted(v_and_t.items(),key=lambda x:x[1])
    v_and_t = dict(v_and_t)

    for v,t in v_and_t.items():
        if t >= 0:
            current_v = v
            start_t = t
            break
    times = []
    try:
        while s <= 4.5:
            v_and_t = {v:t for v,t in v_and_t.items() if v > current_v}
            delta_ts = []
            for v,t in v_and_t.items():
                delta_t = (v*t - current_v*start_t)/(3600*(v-current_v))
                delta_ts.append((v,delta_t))
            delta_ts.sort(key=lambda x:x[1])
            times.append(delta_ts[0][1])
            s += current_v*(delta_ts[0][1]-start_t)
            current_v = delta_ts[0][0]
            start_t = v_and_t[current_v]
    except IndexError:
        times.append((4.5-s)/current_v*3600)
print(ceil(sum(times)))







