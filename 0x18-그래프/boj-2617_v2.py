import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

heavy = [[] for _ in range(N + 1)]
light = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    heavy[v].append(u)
    light[u].append(v)


def bfs(heavy, light, start, N):
    q = deque()
    visited = [False] * (N + 1)
    q.append(start)
    visited[start] = True
    cnt = -1
    while q:
        node = q.popleft()
        cnt += 1
        for nxt in heavy[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

    if cnt > (N - 1) // 2:
        return True

    q = deque()
    visited = [False] * (N + 1)
    q.append(start)
    visited[start] = True
    cnt = -1
    while q:
        node = q.popleft()
        cnt += 1
        for nxt in light[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

    if cnt > (N - 1) // 2:
        return True

    return False


cnt = 0
for i in range(1, N + 1):
    result = bfs(heavy, light, i, N)
    if result:
        cnt += 1

print(cnt)
