n = int(input())
while n != 1:
    if n % 2 == 1:
        old = n
        n = n * 3 + 1
        print('{}*3+1={}'.format(old,n))
    else:
        old = n
        n = n // 2
        print('{}/2={}'.format(old,n))
print('End')