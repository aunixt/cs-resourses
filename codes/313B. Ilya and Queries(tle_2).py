s = input()
possible_i = []
for x in range(len(s)-1):
    if s[x] == s[x+1]:
        possible_i.append(x+1)
m = int(input())
for _ in range(m):
    j, r = map(int, input().split())
    num_of_i = 0
    for i in range(j,r):
        if i in possible_i:
            num_of_i += 1
    print(num_of_i)