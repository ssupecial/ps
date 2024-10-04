n, m = list(map(int, input().split()))
numbers = sorted(set(list(map(int, input().split()))))
arr = []


def func(depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for num in numbers:
        arr.append(num)
        func(depth + 1)
        arr.pop()


func(0)
