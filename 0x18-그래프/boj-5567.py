import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
depth = [-1] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

depth[1] = 0
q = deque()
q.append(1)
answer = 0

while q:
    node = q.pop()
    cur_depth = depth[node]

    if cur_depth <= 1:
        for nxt in adj[node]:
            if depth[nxt] == -1:
                answer += 1
                q.append(nxt)
                depth[nxt] = cur_depth + 1

print(answer)
