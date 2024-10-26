import sys
import heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]
dist = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append([w, v])
    dist[u][v] = w


def dijkstra(start):
    d = [float("inf")] * (N + 1)
    d[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        weight, node = heapq.heappop(q)
        if d[node] != weight:
            continue
        for w, nxt in adj[node]:
            if d[node] + w < d[nxt]:
                d[nxt] = d[node] + w
                heapq.heappush(q, [d[nxt], nxt])

    return d


dist_from_start = dijkstra(X)
results = []
for i in range(1, N + 1):
    if i != X:
        paths = dijkstra(i)
        results.append(dist_from_start[i] + paths[X])


print(max(results))
