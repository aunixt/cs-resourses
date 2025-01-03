l, m = map(int, input().split())
r = [(0, l)]  # 初始化为整个区间
left = 0

for _ in range(m):
    a, b = map(int, input().split())

    new_r = []  # 新的区间列表
    removed = False  # 标记是否已经处理了区间

    for start, end in r:
        if a >= start and b <= end:  # 区间完全包含在现有区间内
            # 分割区间
            if a > start:
                new_r.append((start, a - 1))
            if b < end:
                new_r.append((b + 1, end))
            removed = True
        else:  # 区间部分重叠或不重叠
            if end < a or b < start:  # 区间不重叠
                new_r.append((start, end))
            else:  # 区间部分重叠
                if a > start:
                    new_r.append((start, a - 1))
                if b < end:
                    new_r.append((b + 1, end))
                removed = True

    # 如果区间未被处理，则添加新区间
    if not removed:
        new_r.append((a, b))

    r = new_r  # 更新区间列表

# 计算剩余树木的数量
for start, end in r:
    left += end - start + 1

print(left)