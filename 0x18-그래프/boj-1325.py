import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[v].append(u)


def count(adj, start, N):
    q = deque()
    visited = [False] * (N + 1)
    visited[start] = True
    q.append(start)
    cnt = 0
    while q:
        node = q.popleft()
        for nxt in adj[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                cnt += 1

    return cnt


max_cnt = 0
answer = []
for i in range(1, N + 1):
    tmp = count(adj, i, N)
    if max_cnt == tmp:
        answer.append(i)
    elif max_cnt < tmp:
        max_cnt = tmp
        answer.clear()
        answer.append(i)

print(*answer)
