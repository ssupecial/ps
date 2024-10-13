from collections import deque

n, m = map(int, input().split())

indegrees = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    indegrees[v] += 1

q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end=" ")
    for nxt in adj[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)
