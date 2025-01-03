results = []
while True:
    n = float(input())
    if n == 0:
        break
    ret = 0
    i = 2
    while True:
        ret += 1/i
        if ret > n:
            break
        i +=1
    results.append(i-1)
for x in results:
    print(x,'card(s)')
