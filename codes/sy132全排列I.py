def qpl(idx,n,used,seq,ret):
    if idx == n+1:
        ret.append(seq[:])
        return
    else:
        for i in range(1,n+1):
            if not used[i]:
                seq.append(str(i))
                used[i] = True
                qpl(idx+1,n,used,seq,ret)
                used[i] = False
                seq.pop()

idx = 1
n = int(input())
used = [False]*(n+1)
seq = []
ret = []
qpl(idx,n,used,seq,ret)
for i in ret:
    print(' '.join(i))