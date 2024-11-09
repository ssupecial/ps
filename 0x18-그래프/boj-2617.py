import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

paths = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    paths[i][i] = 0

for _ in range(M):
    u, v = map(int, input().split())
    paths[v][u] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if paths[j][i] + paths[i][k] < paths[j][k]:
                paths[j][k] = paths[j][i] + paths[i][k]

reverse = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        reverse[i][j] = paths[j][i]

answer = 0
for i in range(1, N + 1):
    tmp = paths[i][1:i] + paths[i][i + 1 :]
    cnt = 0
    for value in tmp:
        if value != float("inf"):
            cnt += 1

    if cnt > N // 2:
        answer += 1
        continue

    tmp = reverse[i][1:i] + reverse[i][i + 1 :]
    cnt = 0
    for value in tmp:
        if value != float("inf"):
            cnt += 1

    if cnt > N // 2:
        answer += 1

print(answer)
