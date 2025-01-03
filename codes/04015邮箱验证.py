while True:
    try:
        n = input()
        flag1, flag2, flag3_1, flag3_2 = False, False, False, False

        if n.count('@') == 1:
            flag1 = True

        if n[0] != '@' and n[0] != '.' and n[-1] != '@' and n[-1] != '.':
            flag2 = True

        x = n.split('@')
        for i in range(1,len(x)):
            if '.' in x[i]:
                flag3_1 = True
                break

        if '.@' not in n and '@.' not in n:
            flag3_2 = True

        if flag1 and flag2 and flag3_1 and flag3_2:
            print('YES')
        else:
            print('NO')

    except EOFError:
        break
    except IndexError:
        break

