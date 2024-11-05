import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited[1] = True
answer = 0
q = deque()
q.append(1)
while q:
    node = q.pop()
    for nxt in adj[node]:
        if not visited[nxt]:
            answer += 1
            q.append(nxt)
            visited[nxt] = True

print(answer)
