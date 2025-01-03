k = int(input())
input_str = input()
new_str = ''
for i in input_str:
    if 'A' <= i <='Z':
        index = ord(i) - k
        while index < 65:
            index += 26
        while index > 90:
            index -= 26
        new_str += chr(index)
    if 'a' <= i <='z':
        index = ord(i) - k
        while index < 97:
            index += 26
        while index > 122:
            index -= 26
        new_str += chr(index)
print(new_str)