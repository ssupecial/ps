n, m = list(map(int, input().split()))
numbers = sorted(list(map(int, input().split())))
arr = []

def func(depth, index):
    if depth == m:
        print(" ".join(map(str, arr)))
        return 

    cur = 0
    for i in range(index, n):
        if numbers[i] != cur:
            arr.append(numbers[i])
            func(depth+1, i+1)
            arr.pop()
            cur = numbers[i]
    
func(0, 0)
