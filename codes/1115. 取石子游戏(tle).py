from functools import lru_cache

@lru_cache()
def can_win(a, b):
    if b == 0:
        return True
    for i in range(1, a//b+1):
        if not can_win(max(a-i*b, b), min(a-i*b, b)):
            return True
    return False

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a == b:
        print('win')
        continue
    if a < b:
        a, b = b, a
    print('win' if can_win(a, b) else 'lose')