y = int(input())
if y % 3200 == 0:
    print("N")
elif y % 3200 != 0 and y % 400 != 0 and y % 100 == 0:
    print("N")
elif y % 4 == 0:
    print("Y")
else:
    print("N")
