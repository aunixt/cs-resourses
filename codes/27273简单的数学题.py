import math
n = int(input())
for _ in range(n):
    x = int(input())
    ret = (1+x)*x//2-2*(2**(math.floor(math.log2(x))+1)-1)
    print(ret)