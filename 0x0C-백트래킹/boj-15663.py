n, m = list(map(int, input().split()))
numbers = sorted(list(map(int, input().split())))
arr = []
len_numbers = len(numbers)
issued = [False for _ in range(len_numbers)]


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    cur = 0
    for i in range(0, len_numbers):
        if numbers[i] != cur and not issued[i]:
            arr.append(numbers[i])
            issued[i] = True
            func(depth + 1)
            arr.pop()
            issued[i] = False
            cur = numbers[i]


func(0)
