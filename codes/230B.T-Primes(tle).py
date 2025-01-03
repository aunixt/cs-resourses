import math

def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

n = int(input())
ls = list(map(int, input().split()))
for i in ls:
    if math.sqrt(i) % 1 != 0:
        print('NO')
        continue
    else:
        x = int(math.sqrt(i))
        if isprime(x):
            print('YES')
        else:
            print('NO')