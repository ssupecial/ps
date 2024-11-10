import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
k = tmp[0]
truths = tmp[1:]
party_list = []
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    num = tmp[0]
    people = tmp[1:]
    party_list.append(people)

    for i in range(num - 1):
        adj[people[i]].append(people[i + 1])
        adj[people[i + 1]].append(people[i])

# 진실을 알 수 있는 사람들을 모두 찾아내기
visited = [False] * (N + 1)
for start in truths:
    if visited[start]:
        continue

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        for nxt in adj[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True


cnt = 0
for people in party_list:
    talk = True
    for person in people:
        if visited[person]:
            talk = False
            break

    if talk:
        cnt += 1

print(cnt)
