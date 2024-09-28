def lsm(x, y):
    a = max(x, y)
    b = min(x, y)
    while b >= 1:
        tmp = b
        b = a % b
        a = tmp

    return x * y // a


def check(m, n, x, y):
    N = lsm(m, n)
    start = x
    if m == 1 and n == 1:
        return 1

    while start <= N:
        if start % n == y:
            return start
        start += m

    return -1


num = int(input())
for i in range(num):
    m, n, x, y = list(map(int, input().split()))
    print(check(m, n, x, y))
