from functools import lru_cache

@lru_cache(maxsize=None)
def f(i,j):
    if i == N-1:
        return tri[i][j]
    return max(f(i+1,j),f(i+1,j+1)) + tri[i][j]

N = int(input())
tri = []
for _ in range(N):
    tri.append([int(x) for x in input().split()])
print(f(0,0))