n, m = list(map(int, input().split()))
numbers = sorted(set(list(map(int, input().split()))))
len_numbers = len(numbers)
arr = []


def func(depth, index):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(index, len_numbers):
        arr.append(numbers[i])
        func(depth + 1, i)
        arr.pop()


func(0, 0)
