n, w = map(int,input().split())
values = []
weights = []
average_value = []
sum_value = 0
sum_weight = 0
flag = False
for _ in range(n):
    value, weight = map(int,input().split())
    values.append(value)
    weights.append(weight)
for i in range(n):
    average_value.append((i, values[i]/weights[i]))
average_value.sort(reverse = True, key=lambda x: x[1])
for j in range(n):
    sum_weight += weights[average_value[j][0]]
    sum_value += values[average_value[j][0]]
    if sum_weight == w:
        print('{:.1f}'.format(sum_value))
        flag = True
        break
    elif sum_weight > w:
        print('{:.1f}'.format(sum_value - (sum_weight - w)*average_value[j][1]))
        flag = True
        break
if not flag:
    print('{:.1f}'.format(sum_value))
