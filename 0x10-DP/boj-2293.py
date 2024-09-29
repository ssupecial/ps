# 00:45~실패
n, k = list(map(int, input().split()))
arr = [0] * (k+1)


coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

arr[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        arr[i] = arr[i] + arr[i-coin]

print(arr[k])