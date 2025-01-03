n = int(input())
coins = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
for _ in range(n):
    true_coins = set()
    light_set = set()
    heavy_set = set()
    for _ in range(3):
        a, b, c = input().split()
        if c == 'even':
            true_coins = true_coins.union(set(a), set(b))
        elif c == 'up':
            light_set = light_set.union(set(b))
            heavy_set = heavy_set.union(set(a))
        elif c == 'down':
            light_set = light_set.union(set(a))
            heavy_set = heavy_set.union(set(b))
    wrong_in_it1 = light_set.difference(heavy_set)
    wrong_in_it1 = wrong_in_it1.union(heavy_set.difference((light_set)))
    wrong_in_it2 = coins.difference(true_coins)
    wrong = wrong_in_it2.intersection(wrong_in_it1)
    for i in wrong:
        if i in light_set:
            print('{} is the counterfeit coin and it is {}. '.format(i, 'light'))
            break
        elif i in heavy_set:
            print('{} is the counterfeit coin and it is {}. '.format(i, 'heavy'))
            break

