n = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = [x for x in n if x not in vowels]
print('.'+'.'.join(consonants))
