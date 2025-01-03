def has_odd_divisor(n):
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 'NO'
    return 'YES'

t = int(input())
ret = []
for _ in range(t):
    n = int(input())
    ret.append(has_odd_divisor(n))
print('\n'.join(ret))
