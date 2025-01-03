n = int(input())
p = input().split()
total = 0
for i in range(n):
    total += int(p[i])
average = total / n
print(average)
