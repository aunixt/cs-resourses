n = int(input())
coins = list(map(int, input().split()))
total = sum(coins)
my_money = 0
coins.sort(reverse=True)
for i in range(n):
    my_money += coins[i]
    if my_money > total - my_money:
        break
print(i + 1)
