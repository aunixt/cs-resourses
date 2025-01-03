lucky_nums = [4,7,44,47,77,444,447,474,744,477,747,774,777]
n = int(input())
flag = False
for i in lucky_nums:
    if n % i == 0:
        flag = True
        break
print('YES' if flag else 'NO')