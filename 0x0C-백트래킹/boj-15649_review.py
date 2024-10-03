n, m = list(map(int, input().split()))
check = [False for _ in range(n + 1)]
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if not check[i]:
            check[i] = True
            arr.append(i)
            func(depth + 1)
            check[i] = False
            arr.pop()


func(0)
