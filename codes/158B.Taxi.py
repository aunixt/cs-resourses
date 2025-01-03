import math
n = int(input())
ls = list(map(int, input().split()))
a, b, c, d = 0, 0, 0, 0
car_num = 0
for i in ls:
    if i == 1:
        a += 1
    elif i == 2:
        b += 1
    elif i == 3:
        c += 1
    elif i == 4:
        d += 1

if c >= a:
    car_num = d + math.ceil(b/2) + c
else:
    if b % 2 == 0:
        car_num = d + c + b//2 +math.ceil((a-c)/4)
    else:
        car_num = d + c + math.ceil(b/2) + math.ceil((a-c-2)/4)
print(car_num)