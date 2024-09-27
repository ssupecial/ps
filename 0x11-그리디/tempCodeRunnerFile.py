n, k = list(map(int, input().split()))

coins = []
index = None
for i in range(n):
    coin = int(input())
    coins.append(coin)
    if coin < k:
        index = i

num = 0
while k > 0:
    coin = coins[index]
    if coin <= k:
        need_count = k // coin
        num += need_count
        k -= need_count * coin

    index -= 1


print(num)
