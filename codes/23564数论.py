def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

x = int(input())
result = {}
divisor = 2
num = 0
while x != 1:
    while x % divisor == 0 and isPrime(divisor):
        result[divisor] = result.get(divisor, 0) + 1
        x //= divisor
    divisor += 1

flag = False
for j in sorted(result.values()):
    if j > 1:
        flag = True
        break
if flag:
    print(0)
else:
    if sum(result.values()) % 2 == 0:
        print(1)
    else:
        print(-1)
