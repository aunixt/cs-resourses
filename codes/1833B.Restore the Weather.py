def match_temperatures(a, b, k):
    a_sorted = sorted(enumerate(a), key=lambda x: x[1])
    b_sorted = sorted(enumerate(b), key=lambda x: x[1])

    result = [-1] * len(a)
    used = [False] * len(b)

    for i, temp_a in a_sorted:
        for j, temp_b in b_sorted:
            if not used[j] and abs(temp_a - temp_b) <= k:
                result[i] = str(temp_b)
                used[j] = True
                break
    return result

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(' '.join(match_temperatures(a, b, k)))
