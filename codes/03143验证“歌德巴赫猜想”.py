def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

x = int(input())
if x < 6 or x % 2 == 1:
    print('Error!')
else:
    for i in range(2, x//2+1):
        if isPrime(i) and isPrime(x-i):
            print('{}={}+{}'.format(x,i,x-i))