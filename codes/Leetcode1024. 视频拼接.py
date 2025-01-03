clips = eval(input())
clips.sort()
time = int(input())

def count(start, end):
    cnt = 0
    max_r = 0
    for clip in clips:
        l, r = clip[0], clip[1]
        if l <= start:
            max_r = max(max_r, r)
        else:
            start = max_r
            cnt += 1
            if l > start:
                return -1
            max_r = r
        if max_r >= end:
            cnt += 1
            return cnt
    return -1

print(count(0, time))