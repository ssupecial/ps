import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]


q = deque()

not_tomato = 0
for i in range(H):
    for j in range(N):
        tmp = list(map(int, input().split()))
        for k in range(M):
            if tmp[k] == 0:
                not_tomato += 1
            if tmp[k] == 1:
                q.append([i, j, k, 0])
                visited[i][j][k] = 0
            board[i][j][k] = tmp[k]

dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

max_day = 0

while q:
    x, y, z, day = q.popleft()
    for i in range(6):
        cur_x = x + dx[i]
        cur_y = y + dy[i]
        cur_z = z + dz[i]

        if (
            cur_x < 0
            or cur_x >= H
            or cur_y < 0
            or cur_y >= N
            or cur_z < 0
            or cur_z >= M
        ):
            continue

        if visited[cur_x][cur_y][cur_z] != -1:
            continue

        if board[cur_x][cur_y][cur_z] != 0:
            continue

        q.append([cur_x, cur_y, cur_z, day + 1])
        visited[cur_x][cur_y][cur_z] = day + 1
        not_tomato -= 1

        if max_day < (day + 1):
            max_day = day + 1


answer = -1 if not_tomato != 0 else max_day
print(answer)
