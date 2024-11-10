import sys

input = sys.stdin.readline

N, M = map(int, input().split())
roots = [-1] * (N + 1)


def find(x):
    tmp = x
    while roots[x] >= 0:
        x = roots[x]
    root = x

    x = tmp
    while roots[x] >= 0:
        nxt = roots[x]
        roots[x] = root
        x = nxt

    return root


def union(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return
    roots[u] = v
    return


for _ in range(M):
    operand, u, v = map(int, input().split())
    if operand == 0:  # 합집합
        union(u, v)
    else:  # Union인지 확인
        u = find(u)
        v = find(v)
        if u == v:
            print("YES")
        else:
            print("NO")
