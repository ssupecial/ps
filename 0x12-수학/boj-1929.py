m, n = list(map(int, input().split()))
arr = [True] * (n + 1)
arr[1] = False

for i in range(2, n + 1):
    j = i * i
    while j <= n:
        arr[j] = False
        j = j + i

for i in range(m, n + 1):
    if arr[i]:
        print(i)
