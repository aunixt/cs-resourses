n = int(input())
for _ in range(n):
    x = int(input())

    if x == 1:
        print(0)
        continue

    flag1 = True
    num_of_3 = 0
    while flag1:
        if x % 3 == 0:
            num_of_3 += 1
            x = x // 3
        else:
            flag1 = False

    flag2 = True
    num_of_2 = 0
    while flag2:
        if x % 2 == 0:
            num_of_2 += 1
            x = x // 2
        else:
            flag2 = False

    if x != 1 or num_of_3 < num_of_2:
        print(-1)
    else:
        if num_of_3 > num_of_2:
            print(2 * num_of_3 - num_of_2)
        else:
            print(num_of_3)



