from collections import deque

n = int(input())
adj = [[] for _ in range(n + 1)]

parents = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

q = deque([1])

while q:
    cur_node = q.pop()
    for nxt in adj[cur_node]:
        if nxt != parents[cur_node]:
            parents[nxt] = cur_node
            q.append(nxt)

for parent in parents[2:]:
    print(parent)
