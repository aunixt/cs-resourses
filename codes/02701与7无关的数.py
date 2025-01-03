n = int(input())
square_sum = 0
for i in range(1,n+1):
    if i % 7 != 0 and '7' not in str(i):
        square_sum += i**2
print(square_sum)