from math import sqrt
n = int(input())
for _ in range(n):
    a, b, c = map(float, input().split())
    if b == 0:
        b = -b
    delta = b**2 - 4*a*c
    if delta < 0:
        R = -b/(2*a)
        I = sqrt(-delta)/(2*a)
        x1 = '{:.5f}+{:.5f}i'.format(R, I)
        x2 = '{:.5f}-{:.5f}i'.format(R, I)
        print('x1='+x1+';'+'x2='+x2)
    elif delta == 0:
        print('x1=x2={:.5f}'.format(-b/(2*a)))
    else:
        x1 = '{:.5f}'.format((-b+sqrt(delta))/(2 * a))
        x2 = '{:.5f}'.format((-b-sqrt(delta))/(2 * a))
        print('x1='+x1+';'+'x2='+x2)
