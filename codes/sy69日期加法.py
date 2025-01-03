def isRun(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False

def days_per_month(y, m):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and isRun(y):
        return 29
    else:
        return days[m-1]

y, m, d = map(int,input().split('-'))
n = int(input())
day = n + d

while True:
    if day <= days_per_month(y, m):
        break
    else:
        day -= days_per_month(y, m)
        m += 1
        if m > 12:
            m = 1
            y += 1

print('{}-{:0>2d}-{:0>2d}'.format(y, m, day))