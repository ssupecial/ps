from collections import deque

edges = []  # [u, v] 2차원 배열이 있다고 가정
n  # 노드의 개수


def topological_tree():
    indegrees = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        indegrees[v] += 1
        adj[u].append(v)

    q = deque()
    for i in range(1, n + 1):
        if indegrees[i] == 0:
            q.append(i)

    answers = []

    while q:
        node = q.popleft()
        answers.append(node)
        for nxt in adj[node]:
            indegrees[nxt] -= 1
            if indegrees[nxt] == 0:
                q.append(nxt)

    check_cycle = True if len(answers) != n else False
