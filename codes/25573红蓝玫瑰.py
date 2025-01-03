roses = input()
n = len(roses)
rdp = [0] * n
bdp = [0] * n
if roses[0] == 'R':
    bdp[0] = 1
else:
    rdp[0] = 1

for i in range(1, n):
    if roses[i] == 'R':
        rdp[i] = min(rdp[i-1], bdp[i-1]+1)
        bdp[i] = min(rdp[i-1]+1, bdp[i-1]+1)
    else:
        rdp[i] = min(bdp[i-1]+1, rdp[i-1]+1)
        bdp[i] = min(bdp[i-1], rdp[i-1]+1)

print(rdp[n-1])