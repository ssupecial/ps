from collections import deque

n, m = map(int, input().split())

indegrees = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    orders = list(map(int, input().split()))[1:]
    for i in range(len(orders) - 1):
        indegrees[orders[i + 1]] += 1
        adj[orders[i]].append(orders[i + 1])

q = deque()
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)

results = []
while q:
    node = q.popleft()
    results.append(node)
    for nxt in adj[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)


if len(results) != n:
    print(0)
else:
    for result in results:
        print(result)
