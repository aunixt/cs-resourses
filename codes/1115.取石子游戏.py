def can_win(a, b, step):
    if a == b:
        return True
    elif a // b >= 2:
        return True
    else:
        new_a, new_b = b, a-b
        if new_a // new_b >= 2:
            if step % 2 == 0:
                return False
            else:
                return True
        else:
            return can_win(new_a, new_b, step+1)

while True:
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    if a == b == 0:
        break
    print('win' if can_win(a, b, 0) else 'lose')