import sys

input = sys.stdin.readline
M, N = map(int, input().split())

space = []
for _ in range(M):
    arr = list(map(int, input().split()))
    ranks = {size: i for i, size in enumerate(sorted(list(set(arr))))}
    tmp = [ranks[size] for size in arr]
    space.append(tmp)

answer = 0
for i in range(M - 1):
    first = space[i]
    for j in range(i + 1, M):
        second = space[j]
        if first == second:
            answer += 1


print(answer)
