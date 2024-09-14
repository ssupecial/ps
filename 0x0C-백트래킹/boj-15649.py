n = None
m = None
arr = []
isused = []


def func(k):
    global n, m, arr, isused

    if k == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if not isused[i]:
            arr.append(i)
            isused[i] = 1
            func(k + 1)
            arr.pop()
            isused[i] = 0


if __name__ == "__main__":
    n, m = list(map(int, input().split(" ")))

    arr = []
    isused = [0] * (n + 1)

    func(0)
