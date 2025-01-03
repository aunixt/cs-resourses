situation = input()
l = []
for i in range(len(situation)-6):
    test = situation[i:i+7]
    l.append(test)
if '0000000' in l or '1111111' in l:
    print('YES')
else:
    print('NO')
