s = input()
n = ''
for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        n += chr(ord(s[i]) + 32)
    elif 'a' <= s[i] <= 'z':
        n += chr(ord(s[i]) - 32)
    else:
        n += s[i]
print(n)
