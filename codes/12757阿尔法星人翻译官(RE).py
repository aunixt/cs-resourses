dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
        'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18,
        'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}

def ten_transform(eng):
    eng = eng.split()
    ret = 0
    if len(eng) == 2:
        for i in range(len(eng)):
            ret += dict[eng[i]]
    else:
        ret = dict[eng[0]]
    return ret

def hundred_transform(eng):
    ret = 0
    eng = eng.split(' hundred ')
    if len(eng) > 1:
        ret += dict[eng[0]] * 100
        ret += ten_transform(eng[1])
    else:
        ret = ten_transform(eng[0])
    return ret

s = [input()]
flag1 = flag2 = False
ans = ''

if 'negative' in s[0]:
    ans += '-'
    s[0] = s[0].replace('negative ', '')
if 'million' in s[0]:
    flag1 = True
    s.append(s[0].split(' million ')[1])
    s[0] = s[0].split(' million ')[0]
if 'thousand' in s[-1]:
    flag2 = True
    s.append(s[-1].split(' thousand ')[1])
    s[-2] = s[-2].split(' thousand ')[0]

if len(s) == 1:
    if flag1:
        print(ans + str(hundred_transform(s[0])*1000000))
    elif flag2:
        print(ans + str(hundred_transform(s[0])*1000))
    else:
        print(ans + str(hundred_transform(s[0])))
elif len(s) == 2:
    if flag1 and flag2:
        print(ans + str(hundred_transform(s[0]) * 1000000 + hundred_transform(s[1])*1000))
    elif flag1 and not flag2:
        print(ans + str(hundred_transform(s[0])*1000000 + hundred_transform(s[1])))
    elif not flag1 and flag2:
        print(ans + str(hundred_transform(s[0])*1000 + hundred_transform(s[1])))
elif len(s) == 3:
    print(ans + str(hundred_transform(s[0]) * 1000000 + hundred_transform(s[1]) * 1000 + hundred_transform(s[2]) * 1000))

