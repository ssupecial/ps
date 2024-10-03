n, m = list(map(int, input().split()))
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        arr.append(i)
        func(depth + 1)
        arr.pop()


func(0)
