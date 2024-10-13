n = int(input())
parents = [0] * (27)
lcs = [0] * (27)
rcs = [0] * (27)
base_chr = ord("A") - 1
for _ in range(n):
    cur, lc, rc = map(lambda x: max(0, ord(x) - ord("A") + 1), input().split())
    parents[lc] = cur
    parents[rc] = cur
    lcs[cur] = lc
    rcs[cur] = rc


def level(node):
    print(chr(node + base_chr), end="")
    if lcs[node]:
        level(lcs[node])
    if rcs[node]:
        level(rcs[node])


level(1)
print()


def left(node):
    if lcs[node]:
        left(lcs[node])
    print(chr(node + base_chr), end="")
    if rcs[node]:
        left(rcs[node])


left(1)
print()


def right(node):
    if lcs[node]:
        right(lcs[node])
    if rcs[node]:
        right(rcs[node])
    print(chr(node + base_chr), end="")


right(1)
print()
