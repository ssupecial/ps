import sys

input = sys.stdin.readline

N, M = map(int, input().split())
paths = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    paths[i][i] = 0

for _ in range(M):
    u, v = map(int, input().split())
    paths[u][v] = 1
    paths[v][u] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if paths[j][i] + paths[i][k] < paths[j][k]:
                paths[j][k] = paths[j][i] + paths[i][k]

min_kevin = float("inf")
answer = 0
for i in range(1, N + 1):
    kevin = sum(paths[i][1:i] + paths[i][i + 1 :])
    if kevin < min_kevin:
        min_kevin = kevin
        answer = i

print(answer)
