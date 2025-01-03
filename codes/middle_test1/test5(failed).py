def rom_to_num(n):
    dic1 = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9'}
    dic2 = {'X': '1', 'XX': '2', 'XXX': '3', 'XL': '4', 'L': '5', 'LX': '6', 'LXX': '7', 'LXXX': '8', 'XC': '9'}
    dic3 = {'C': '1', 'CC': '2', 'CCC': '3', 'CD': '4', 'D': '5', 'DC': '6', 'DCC': '7', 'DCCC': '8', 'CM': '9'}
    dic4 = {'M': '1', 'MM': '2', 'MMM': '3'}
    s = []
    num = ''
    indexs = [n.find('M'),min(n.find('C'),n.find('D')),min(n.find('X'),n.find('L')),min(n.find('I'),n.find('V'))]
    indexs = [x for x in indexs if x != -1]
    indexs[0] -= 1
    for i in range(0,len(indexs)-1):
        s.append(n[indexs[i+1]:indexs[i+2]])
    if len(s) == 1:
        num = dic1[s[0]]
    elif len(s) == 2:
        num = dic2[s[0]] + dic1[s[1]]
    elif len(s) == 3:
        num = dic3[s[0]] + dic2[s[1]] + dic1[s[2]]
    elif len(s) == 4:
        num = dic4[s[0]] + dic3[s[1]] + dic2[s[2]] + dic1[s[3]]
    return num

    '''spec = [0,0,0]
    for i in range(0,len(n)-1):
        if n[i] == 'I' and (n[i+1] == 'V' or n[i+1] == 'X'):
            spec[0] += 1
        elif n[i] == 'X' and (n[i+1] == 'L' or n[i+1] == 'C'):
            spec[1] += 1
        elif n[i] == 'C' and (n[i+1] == 'D' or n[i+1] == 'M'):
            spec[2] += 1
    num = n.count('I') + 5*n.count('V') + 10*n.count('X') + 50*n.count('L') + 100*n.count('C') + 500*n.count('D') + 1000*n.count('M') - 2*(spec[0] + 10*spec[1] + 100*spec[2])
    return num'''

def num_to_rom(n):
    dic1 = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
    dic2 = {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
    dic3 = {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
    dic4 = {'1': 'M', '2': 'MM', '3': 'MMM'}
    rom = ''
    if len(n) == 1:
        rom = dic1[n]
    elif len(n) == 2:
        rom = dic2[n[0]] + dic1[n[1]]
    elif len(n) == 3:
        rom = dic3[n[0]] + dic2[n[1]] + dic1[n[2]]
    elif len(n) == 4:
        rom = dic4[n[0]] + dic3[n[1]] + dic2[n[2]] + dic1[n[3]]
    return rom

n = input()
if n.isdigit():
    print(num_to_rom(n))
else:
    print(rom_to_num(n))



