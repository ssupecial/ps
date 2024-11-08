import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]
while True:
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    if u == -1 and v == -1:
        break


def find_depth(adj, start, N):
    q = deque()
    friends = [-1] * (N + 1)
    q.append(start)
    friends[start] = 0
    while q:
        node = q.popleft()
        depth = friends[node]
        for nxt in adj[node]:
            if friends[nxt] == -1:
                q.append(nxt)
                friends[nxt] = depth + 1

    return max(friends)


results = [N + 2] + [find_depth(adj, i, N) for i in range(1, N + 1)]
score = min(results)
boss = []
for i in range(1, N + 1):
    if results[i] == score:
        boss.append(i)

print(score, len(boss))
print(" ".join(map(str, boss)))
