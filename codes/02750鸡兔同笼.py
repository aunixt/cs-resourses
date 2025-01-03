a = int(input())
if a % 4 == 0:
    print(int(a/4), int(a/2))
elif a % 2 == 0:
    print(int((a+2)/4), int(a/2))
else:
    print(0, 0)
