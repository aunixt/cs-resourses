keyboard = '0qwertyuiop0asdfghjkl;0zxcvbnm,./0'
position = input()
if position == 'R':
    shift = -1
elif position == 'L':
    shift = 1
n = input()
new_str = ''
for i in n:
    letter_index = keyboard.find(i) + shift
    new_str += keyboard[letter_index]
print(new_str)