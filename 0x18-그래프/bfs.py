from collections import deque

v_num = 10
adj = [[] for _ in range(v_num)]
# 인접 리스트를 채웠다고 가정

visited = [False] * v_num
q = deque([])


def bfs():
    q.append(1)  # 시작 정점이 1이라고 가정
    while q:
        node = q.popleft()
        for nxt in adj[node]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
