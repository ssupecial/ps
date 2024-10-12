from collections import deque

v_num = 10
adj = [[] for _ in range(v_num)]
# 인접 리스트를 채웠다고 가정

visited = [False] * v_num


def dfs():  # 비재귀
    q = deque([])
    q.append(1)  # 시작 정점이 1이라고 가정
    while q:
        node = q.pop()
        for nxt in adj[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True


def dfs_():  # 비재귀이나 재귀처럼 동작하도록 (관념적인 DFS)
    q = deque([])
    # 진짜 방문했을 때 방문했다고 표기
    q.append(1)  # 시작 정점이 1이라고 가정
    while q:
        node = q.pop()
        if visited[node]:
            continue
        visited[node] = True

        for nxt in adj[node]:
            if not visited[node]:
                q.append(nxt)


def dfs_recur(cur):
    for nxt in adj[cur]:
        if not visited[nxt]:
            dfs_recur(nxt)
