from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)
answer = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    q = deque([i])
    visited[i] = True
    while q:
        cur = q.pop()
        for next in adj[cur]:
            if visited[next]:
                continue
            q.append(next)
            visited[next] = True
    answer += 1

print(answer)
