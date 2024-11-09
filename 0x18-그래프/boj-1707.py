import sys
from collections import deque

input = sys.stdin.readline


def bfs(adj, visited, start, group):
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        nxt_group = (group[node] + 1) % 2
        for nxt in adj[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                group[nxt] = nxt_group
            elif group[nxt] != nxt_group:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    cnt = 0
    group = [-1] * (V + 1)
    answer = True
    for i in range(1, V + 1):
        if not visited[i]:
            cnt += 1
            visited[i] = True
            group[i] = 0
            answer = bfs(adj, visited, i, group)
            if not answer:
                break

    print("YES") if answer else print("NO")
