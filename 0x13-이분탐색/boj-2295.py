import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    inputs = [int(input()) for _ in range(N)]
    inputs.sort()

    sum_of_two = []
    for i in range(N):
        for j in range(i, N):
            sum_of_two.append(inputs[i] + inputs[j])

    sum_of_two.sort()

    for k in range(N - 1, -1, -1):
        for x in range(0, k):

            if search(sum_of_two, inputs[k] - inputs[x]):
                return inputs[k]


def search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False


answer = solution()
print(answer)
