import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

costs = [[float("inf")] * (n + 1) for _ in range(n + 1)]
nxt = [[-1] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    costs[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(costs[a][b], c)
    nxt[a][b] = b

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if costs[j][k] > costs[j][i] + costs[i][k]:
                costs[j][k] = costs[j][i] + costs[i][k]
                nxt[j][k] = nxt[j][i]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cost = 0 if costs[i][j] == float("inf") else costs[i][j]
        print(cost, end=" ")
    print()


def traverse(s, t):
    results = []
    while s != t:
        results.append(s)
        s = nxt[s][t]
    results.append(t)
    print(f"{len(results)} {' '.join(map(str, results))}")


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if costs[i][j] == 0 or costs[i][j] == float("inf"):
            print(0)
        else:
            traverse(i, j)
