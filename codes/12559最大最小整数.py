n = int(input())
ls = input().split()
for i in range(n):
    for j in range(i+1,n):
        if ls[j] + ls[i] > ls[i] + ls[j]:
            ls[j], ls[i] = ls[i], ls[j]
ls_r = [x for x in ls]
ls_r.reverse()
print(''.join(ls),''.join(ls_r))