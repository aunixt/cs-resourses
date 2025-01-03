def rom_to_num(n):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    pre_num = 0
    for i in reversed(n):
        if romans[i] < pre_num:
            num -= romans[i]
        else:
            num += romans[i]
            pre_num = romans[i]
    return num

def num_to_rom(n):
    rom = ''
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
               rom += sym[i]
               n -= val[i]
        i += 1
    return rom

n = input()
if n.isdigit():
    print(num_to_rom(int(n)))
else:
    print(rom_to_num(n))