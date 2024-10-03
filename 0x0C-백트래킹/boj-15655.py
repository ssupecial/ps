n, m = list(map(int, input().split()))
numbers = sorted(list(map(int, input().split())))
len_numbers = len(numbers)
issued = [False for _ in range(len_numbers)]
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    start = -1 if len(arr) == 0 else numbers.index(arr[-1])

    for i in range(start + 1, len_numbers):
        if not issued[i]:
            arr.append(numbers[i])
            issued[i] = True
            func(depth + 1)
            arr.pop()
            issued[i] = False


func(0)
