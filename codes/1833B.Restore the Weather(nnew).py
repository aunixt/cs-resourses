def match_temperatures(a, b, k):
    a_sorted = sorted(enumerate(a), key=lambda x: x[1])
    b_sorted = sorted(enumerate(b), key=lambda x: x[1])

    result = [-1] * len(a)
    used = [False] * len(b)
    j = 0  # 指向 b_sorted 的起始位置

    for i, temp_a in a_sorted:
        found = False
        while j < len(b_sorted) and not found:
            _, temp_b = b_sorted[j]
            if not used[b_sorted[j][0]] and abs(temp_a - temp_b) <= k:
                result[i] = str(temp_b)
                used[b_sorted[j][0]] = True
                found = True
            elif temp_b < temp_a - k or (j > 0 and temp_b == temp_a - k):  # 不需要再向前看了
                break
            j += 1
    return result

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(' '.join(match_temperatures(a, b, k)))