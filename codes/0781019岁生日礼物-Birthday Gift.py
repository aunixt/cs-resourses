n = int(input())
for _ in range(n):
    s = input()
    if int(s) % 19 == 0 or '19' in s:
        print('Yes')
    else:
        print('No')