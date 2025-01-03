s = input()
m = int(input())
for _ in range(m):
    num_of_i = 0
    l, r = map(int,input().split())
    for i in range(l,r):
        if s[i-1] == s[i]:
            num_of_i += 1
    print(num_of_i)