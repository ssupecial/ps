# 10.15 화요일 22:50~23:00
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
indegrees = [0] * (n + 1)
childs = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    indegrees[v] += 1
    childs[u].append(v)

avails = []
for i in range(1, n + 1):
    if indegrees[i] == 0:
        heapq.heappush(avails, i)

while avails:
    node = heapq.heappop(avails)
    print(node, end=" ")
    for nxt in childs[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            heapq.heappush(avails, nxt)
