n = int(input())
strings = []
a_string = ''
for _ in range(n):
    line = input().split()
    for i in line:
        if '#' in i:
            a_string += i.strip('#')
        else:
            if not a_string:
                continue
            else:
                strings.append(a_string)
                a_string = ''
ret = len(strings)
if a_string:
    ret += 1
print(ret)
