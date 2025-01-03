from math import ceil
dic_of_3 = {0: 0, 1: 5, 2: 3, 3: 1}

while True:
    a, b, c, d, e, f = map(int, input().split())
    if a + b + c + d + e + f == 0:
        break
    boxes = f + e + d + ceil(c/4)

    space_for_2 = 5*d + dic_of_3[c%4]
    if space_for_2 < b:
        boxes += ceil((b-space_for_2)/9)

    space_for_1 = 36*boxes - 36*f - 25*e - 16*d - 9*c - 4*b
    if space_for_1 < a:
        boxes += ceil((a-space_for_1)/36)

    print(boxes)