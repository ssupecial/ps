import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

costs = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    costs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(costs[a][b], c)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if costs[j][k] > costs[j][i] + costs[i][k]:
                costs[j][k] = costs[j][i] + costs[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cost = 0 if costs[i][j] == float("inf") else costs[i][j]
        print(cost, end=" ")
    print()
