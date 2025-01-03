from functools import lru_cache

@lru_cache(maxsize=None)
def f(x):
    if x <= 2:
        return 1
    return f(x-1) + f(x-2)
n = int(input())
for _ in range(n):
    print(f(int(input())))