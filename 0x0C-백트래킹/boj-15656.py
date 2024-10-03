n, m = list(map(int, input().split()))
numbers = sorted(list(map(int, input().split())))
len_numbers = len(numbers)
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(0, len_numbers):
        arr.append(numbers[i])
        func(depth + 1)
        arr.pop()


func(0)
