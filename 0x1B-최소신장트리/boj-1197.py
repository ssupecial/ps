import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(0, v + 1)]
edges = []
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

edges.sort(key=lambda x: x[2])


def get_parent(u):
    if parent[u] == u:
        return u
    parent[u] = get_parent(parent[u])
    return parent[u]


ans = 0
for u, v, w in edges:
    u_p = get_parent(u)
    u_v = get_parent(v)
    if u_p == u_v:
        continue
    else:
        ans += w
        if u_p < u_v:
            parent[u_v] = u_p
        else:
            parent[u_p] = u_v

print(ans)
