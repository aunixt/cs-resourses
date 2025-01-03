s = input()
x = 'hello'
i = 0
for word in s:
    if word == x[i]:
        i += 1
    if i == 5:
        break
if i == 5:
    print('YES')
else:
    print('NO')