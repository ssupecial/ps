import sys

input = sys.stdin.readline


# def find(x, roots):
#     tmp = x
#     while roots[x] != -1:
#         x = roots[x]
#     root = x

#     # 경로 압축
#     x = tmp
#     while roots[x] != -1:
#         nxt = roots[x]
#         roots[x] = root
#         x = nxt

#     return root


def find(x, roots):
    if roots[x] < 0:
        return x
    roots[x] = find(roots[x], roots)
    return roots[x]


def union(u, v, roots):
    u = find(u, roots)
    v = find(v, roots)

    if u == v:
        return

    roots[u] = v


T = int(input())
for t in range(T):
    print(f"Scenario {t+1}:")
    N = int(input())
    K = int(input())
    roots = [-1] * (N + 1)
    for _ in range(K):
        u, v = map(int, input().split())
        union(u, v, roots)
    M = int(input())
    for _ in range(M):
        u, v = map(int, input().split())
        answer = 1 if find(u, roots) == find(v, roots) else 0
        print(answer)
    print()
