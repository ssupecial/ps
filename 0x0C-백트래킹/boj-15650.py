n, m = list(map(int, input().split()))
issued = [False for _ in range(n + 1)]
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    start = arr[-1] if len(arr) != 0 else 0
    for i in range(start + 1, n + 1):
        if not issued[i]:
            arr.append(i)
            issued[i] = True
            func(depth + 1)
            arr.pop()
            issued[i] = False


func(0)
