n =int(input())
for i in range(6,n+1):
    if n % i == 0:
        print(int(n/i))
        break
