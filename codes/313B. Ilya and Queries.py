s = input()
ls = [0]
ans = []
total_i = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        total_i += 1
    ls.append(total_i)
m = int(input())
for _ in range(m):
    j, r = map(int,input().split())
    if r - j == 1:
        if s[r-1] == s[j-1]:
            ans.append(str(1))
        else:
            ans.append(str(0))
    else:
        ans.append(str(ls[r-1]-ls[j-1]))
print('\n'.join(ans))