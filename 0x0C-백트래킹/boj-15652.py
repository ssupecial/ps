n, m = list(map(int, input().split()))
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    start = 1 if len(arr) == 0 else arr[-1]

    for i in range(start, n + 1):
        arr.append(i)
        func(depth + 1)
        arr.pop()


func(0)
