n = int(input())
sum = 0
for i in range(n):
    a, b, c = map(int, input().split())
    l = [a, b, c]
    m = l.count(1)
    if m >= 2:
        sum +=1
print(sum)

