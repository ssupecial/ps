from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
names = input().split()
dict_names = {}
for i in range(n):
    dict_names[names[i]] = i

m = int(input())
indegrees = [0] * n
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y = input().split()
    indegrees[dict_names[x]] += 1
    adj[dict_names[y]].append(dict_names[x])

q = deque()
josangs = []
for i in range(n):
    if indegrees[i] == 0:
        q.append(i)
        josangs.append(names[i])

print(len(josangs))
print(" ".join(sorted(josangs)))
results = []
while q:
    node = q.popleft()
    childs = []
    for nxt in adj[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            childs.append(nxt)
            q.append(nxt)

    results.append([names[node], len(childs), childs])

results.sort(key=lambda x: x[0])
for parent, num, childs in results:
    childs = " ".join(sorted([names[child] for child in childs]))
    print(f"{parent} {num} {childs}")
