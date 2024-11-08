import sys

input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
paths = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    nodes = list(map(int, input().split()))
    for j, node in enumerate(nodes):
        if node == 1:
            adj.append(j + 1)
            paths[i + 1][j + 1] = 1


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if paths[j][i] + paths[i][k] < paths[j][k]:
                paths[j][k] = paths[j][i] + paths[i][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(1, end=" ") if paths[i][j] != float("inf") else print(0, end=" ")
    print()
