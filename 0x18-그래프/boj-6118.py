import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

q = deque()
q.append(1)
depths = [-1] * (N + 1)
depths[1] = 0

while q:
    node = q.popleft()
    depth = depths[node]

    for nxt in adj[node]:
        if depths[nxt] == -1:
            depths[nxt] = depth + 1
            q.append(nxt)

max_depth = max(depths)
results = []
for i in range(2, N + 1):
    if depths[i] == max_depth:
        results.append(i)

print(results[0], max_depth, len(results))
