m, n, a = map(int, input().split())
if m % a == 0 and n % a == 0:
    ret=int((m/a)*(n/a))
elif m % a == 0 and n % a != 0:
    ret=int((m/a)*(n//a+1))
elif m % a != 0 and n % a == 0:
    ret=int((m//a+1)*(n/a))
else:
    ret=(m//a+1)*(n//a+1)
print(ret)