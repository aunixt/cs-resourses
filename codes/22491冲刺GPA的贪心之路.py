h = int(input())
m = int(input())
h = 2*h - 0.5 * m
courses = []
ans = 0
for _ in range(m):
    rate, credit = map(float, input().split())
    courses.append((rate, credit, rate*credit))
courses.sort(key = lambda x: (x[2],x[0]), reverse = True)
print(courses)
for rate, credit, multiple in courses:
    left_h = h - 5 / rate
    if left_h < 0:
        ans += multiple * h
        break
    else:
        ans += credit * 5
        h = left_h
print('{:.1f}'.format(ans))