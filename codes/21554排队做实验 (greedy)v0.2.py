n = int(input())
ls = [int(x) for x in input().split()]
seq = []
average_waiting_time = 0
counted_ls = list(enumerate(ls))
counted_ls.sort(key=lambda x: x[1])
for i, j in counted_ls:
    seq.append(i+1)
    average_waiting_time += j*(n-1)
    n -= 1
average_waiting_time = average_waiting_time/len(ls)
print(' '.join(map(str, seq)))
print('{:.2f}'.format(average_waiting_time))