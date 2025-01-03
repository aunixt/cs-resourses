n = int(input())
ls = [int(x) for x in input().split()]
max_end_here = max_so_far = ls[0]
for x in ls[1:]:
    max_end_here = max(x, max_end_here + x)
    max_so_far = max(max_so_far, max_end_here)
print(max_so_far)