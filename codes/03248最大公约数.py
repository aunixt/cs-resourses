from math import gcd
while True:
    try:
        a, b = map(int, input().split())
        print(gcd(a, b))
    except EOFError:
        break