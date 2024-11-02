N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
finish = 0

result = 0
tmp = 0
even = 0

while start < N:
    while tmp <= K and finish < N:
        if arr[finish] % 2 != 0:
            tmp += 1
        else:
            even += 1

        finish += 1

    if even > result:
        result = even

    if arr[start] % 2 == 1:
        tmp -= 1
    else:
        even -= 1
    start += 1


print(result)
