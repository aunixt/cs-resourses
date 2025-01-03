n, k = map(int, input().split())
scores = list(map(int, input().split()))
w = scores[k-1]
num = 0
for i in range(n):
    if scores[i] >= w and scores[i] > 0:
        num += 1
print(num)