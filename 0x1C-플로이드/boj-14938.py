import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
costs = [[float("inf")] * (n + 1) for _ in range(n + 1)]
items = [0] + list(map(int, input().split()))
for _ in range(r):
    a, b, w = map(int, input().split())
    costs[a][b] = min(costs[a][b], w)
    costs[b][a] = min(costs[b][a], w)

for i in range(1, n + 1):
    costs[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if costs[j][k] > costs[j][i] + costs[i][k]:
                costs[j][k] = costs[j][i] + costs[i][k]

results = []
for i in range(1, n + 1):
    tmp = []
    for j in range(1, n + 1):
        if costs[i][j] <= m:
            tmp.append(j)
    results.append(sum(map(lambda x: items[x], tmp)))

print(max(results))
