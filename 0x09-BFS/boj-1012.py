# 16:20~16:30 (10분)
from collections import deque

t = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(t):
    m, n, k = list(map(int, input().split()))
    board = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    veges = []
    for i in range(k):
        x, y = list(map(int, input().split()))
        board[x][y] = 1
        veges.append([x, y])

    answer = 0

    for start_x, start_y in veges:
        if visited[start_x][start_y]:
            continue
        q = deque()
        answer += 1
        q.append([start_x, start_y])
        while q:
            x, y = q.pop()
            for i in range(4):
                cur_x = x + dx[i]
                cur_y = y + dy[i]

                if cur_x < 0 or cur_x >= m or cur_y < 0 or cur_y >= n:
                    continue
                if not visited[cur_x][cur_y] and board[cur_x][cur_y] == 1:
                    q.append([cur_x, cur_y])
                    visited[cur_x][cur_y] = True

    print(answer)
