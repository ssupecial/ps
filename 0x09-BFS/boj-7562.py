import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for t in range(T):
    q = deque()
    L = int(input())
    visited = [[False] * (L) for _ in range(L)]

    start_x, start_y = map(int, input().split())
    q.append([start_x, start_y, 0])
    visited[start_x][start_y] = True

    dest_x, dest_y = map(int, input().split())

    while q:
        x, y, dist = q.popleft()
        if x == dest_x and y == dest_y:
            print(dist)
            break

        for i in range(8):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            if cur_x < 0 or cur_x >= L or cur_y < 0 or cur_y >= L:
                continue
            if visited[cur_x][cur_y]:
                continue

            q.append([cur_x, cur_y, dist + 1])
            visited[cur_x][cur_y] = True
