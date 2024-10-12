from collections import deque
import sys

input = sys.stdin.readline

n, m, start = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    adj[i].sort()


def bfs():
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    answers = []

    while q:
        node = q.popleft()
        answers.append(node)
        for nxt in adj[node]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = True
    print(" ".join(map(str, answers)))


def dfs():
    visited = [False] * (n + 1)
    q = deque([start])
    answers = []

    while q:
        node = q.pop()
        if visited[node]:
            continue
        visited[node] = True
        answers.append(node)

        for nxt in reversed(adj[node]):
            if not visited[nxt]:
                q.append(nxt)

    print(" ".join(map(str, answers)))


dfs()
bfs()
