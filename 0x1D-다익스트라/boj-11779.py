import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

dist = [float("inf") for _ in range(N + 1)]
pre = [-1 for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append([w, v])  # 비용, 정점


start, end = map(int, input().split())
dist[start] = 0
pre[start] = 0
q = []
heapq.heappush(q, [0, start])

while q:
    weight, node = heapq.heappop(q)
    if dist[node] != weight:
        continue

    for w, v in adj[node]:
        if dist[node] + w < dist[v]:
            dist[v] = dist[node] + w
            heapq.heappush(q, [dist[v], v])
            pre[v] = node


path = []


def recur(cur):
    if cur == 0:
        return
    recur(pre[cur])
    path.append(cur)


print(dist[end])
recur(end)
print(len(path))
print(" ".join(map(str, path)))
