import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())

dist = [float("inf") for _ in range(V + 1)]
dist[start] = 0
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append([w, v])

q = []
heapq.heappush(q, [0, start])
while q:
    weight, node = heapq.heappop(q)
    if dist[node] != weight:
        continue

    for weight, nxt in edges[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])


for i in range(1, V + 1):
    if dist[i] != float("inf"):
        print(dist[i])
    else:
        print("INF")
