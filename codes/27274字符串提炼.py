from math import floor,log2
s = input()
n = len(s)
m = floor(log2(n))
ans = ''
i = 0
j = m
while i < j:
    ans += s[2**i-1]
    ans += s[2**j-1]
    i += 1
    j -= 1
if i == j:
    ans += s[2**i-1]
print(ans)