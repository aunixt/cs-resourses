strs = input().split()
dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
        'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18,
        'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90,
        'hundred':100, 'thousand':1000, 'million':1000000}
if strs[0] == 'negative':
    sgn = -1
    strs.pop(0)
else:
    sgn = 1

temp = 0
ans = 0
for i in strs:
    if i in ['thousand', 'million']:
        ans += temp * dict[i]
        temp = 0
        continue
    if i == 'hundred':
        temp *= 100
    else:
        temp += dict[i]
ans += temp
print(ans * sgn)