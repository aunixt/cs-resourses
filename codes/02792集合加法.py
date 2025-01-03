import bisect

n = int(input())
for _ in range(n):
    cnt = 0
    s = int(input())
    a = int(input())
    A = [int(x) for x in input().split()]
    b = int(input())
    B = [int(x) for x in input().split()]
    sorted_B = sorted(B)
    for i in range(len(A)):
        start = bisect.bisect_left(sorted_B, s-A[i])
        end = bisect.bisect_right(sorted_B, s-A[i])
        cnt += end - start
    print(cnt)


