Haab_Calendar = {
    'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4, 'xul': 5, 'yoxkin': 6,
    'mol': 7, 'chen': 8, 'yax': 9, 'zac': 10, 'ceh': 11, 'mac': 12, 'kankin': 13,
    'muan': 14, 'pax': 15, 'koyab': 16, 'cumhu': 17, 'uayet': 18
}

Tzolkin_Calendar = {
    0: 'imix', 1: 'ik', 2: 'akbal', 3: 'kan', 4: 'chicchan', 5: 'cimi',
    6: 'manik', 7: 'lamat', 8: 'muluk', 9: 'ok', 10: 'chuen', 11: 'eb',
    12: 'ben', 13: 'ix', 14: 'mem', 15: 'cib', 16: 'caban', 17: 'eznab',
    18: 'canac', 19: 'ahau'
}

def Haab_to_Tzolkin(Haab_date):
    a, b, c = Haab_date.split()
    a = int(a.strip('.'))
    b = Haab_Calendar[b]
    c = int(c)
    total_days = c * 365 + b * 20 + a
    tzolkin_year = total_days // 260
    tzolkin_day = total_days % 260
    tzolkin_num = tzolkin_day % 13 + 1  # 数字从1到13
    tzolkin_name = Tzolkin_Calendar[tzolkin_day % 20]
    return '{} {} {}'.format(tzolkin_num, tzolkin_name, tzolkin_year)

n = int(input())
print(n)
for _ in range(n):
    print(Haab_to_Tzolkin(input()))