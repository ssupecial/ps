import sys
from collections import deque

input = sys.stdin.readline

sys.setrecursionlimit(10000)
N, K, M = map(int, input().split())

adj = [[] for _ in range(N + M + 1)]
for i in range(N + 1, N + M + 1):
    nodes = list(map(int, input().split()))
    for node in nodes:
        # i: 하이퍼튜브
        # node: 역
        # 역 -> 하이퍼튜브 : 1 / 하이퍼튜브 -> 역 : 0
        adj[i].append((node, 0))
        adj[node].append((i, 1))

# visited: 1번 노드부터 해당 노드까지 가는데 최소 역 수
visited = [float("inf")] * (N + M + 1)
q = deque()
q.append((1, 1))
visited[1] = 1

while q:
    node, dist = q.popleft()
    for nxt, cost in adj[node]:
        if visited[nxt] > dist + cost:
            visited[nxt] = dist + cost
            q.append((nxt, dist + cost))

print(visited[N]) if visited[N] != float("inf") else print(-1)
