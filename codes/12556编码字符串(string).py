x = input().lower()
s = ''
num = 0
for i in range(len(x)):
    if num == 0:
        s = x[i]
        num += 1
    elif x[i] == x[i-1]:
        num += 1
    elif x[i] != x[i-1]:
        print(f'({s},{num})',end = '')
        s = x[i]
        num = 1
print(f'({s},{num})',end = '')