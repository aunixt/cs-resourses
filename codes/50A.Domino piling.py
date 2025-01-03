user_input = input()
values=user_input.split()
value1=int(values[0])
value2=int(values[1])
if value1 % 2 != 0 and value2 % 2 != 0:
    ret=int((value1*value2-1)/2)
else:
    ret=int(value1*value2/2)
print(ret)

#另解：
#m, n = map(int,input().split())
#num = n // 2 * m
#if n % 2 != 0:
#   num += m // 2
#print(num)