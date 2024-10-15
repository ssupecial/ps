# 10.15 화요일 23:05~23:25 (20분)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
indegrees = [0] * (n + 1)
childs = [[] for _ in range(n + 1)]
parents = [[] for _ in range(n + 1)]
parents[1].append(0)
working_time = [0] * (n + 1)

results = [0] * (n + 1)

for i in range(1, n + 1):
    inputs = list(map(int, input().split()))
    working_time[i] = inputs[0]
    indegrees[i] = inputs[1]
    parents[i].extend(inputs[2:])
    for parent in inputs[2:]:
        childs[parent].append(i)

q = deque([])
for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    cur_time = (
        max(list(map(lambda x: results[x], parents[node]))) if parents[node] else 0
    )  # 이전 선후관계들의 최종 작업 시간 목록 (없으면 시작 시간이 0이 됨)
    # 선 관계가 없을 때를 처리 안 해줘서 초반에 에러가 남
    results[node] = cur_time + working_time[node]
    for nxt in childs[node]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)

print(max(results))
