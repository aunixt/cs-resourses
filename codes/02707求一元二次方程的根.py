from math import sqrt
n = int(input())
for _ in range(n):
    a, b, c = map(float, input().split())
    delta = b**2 - 4*a*c
    if delta < 0:
        R_x1 = R_x2 = round(-b/(2*a),5)
        I_x1 = I_x2 = round(sqrt(-delta)/(2*a),5)
        x1 = str(R_x1) + '+' + str(I_x1) + 'i'
        x2 = str(R_x2) + '-' + str(I_x2) + 'i'
        print('x1='+x1+';'+'x2='+x2)
    elif delta == 0:
        print('x1=x2='+str(round(-b/(2*a),5)))
    else:
        x1 = str(round((-b+sqrt(delta))/(2 * a),5))
        x2 = str(round((-b-sqrt(delta))/(2 * a),5))
        print('x1='+x1+';'+'x2='+x2)
