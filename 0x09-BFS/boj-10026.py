import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = []
board2 = []

for _ in range(N):
    inputs = input().strip()
    board.append(list(map(str, inputs)))
    board2.append(list(map(str, inputs.replace("G", "R"))))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = []
# 적록색약이 아님
visited = [[False] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        q = deque()
        q.append([i, j, board[i][j]])
        visited[i][j] = True
        cnt += 1
        while q:
            x, y, color = q.popleft()
            for k in range(4):
                cur_x = x + dx[k]
                cur_y = y + dy[k]
                if cur_x < 0 or cur_x >= N or cur_y < 0 or cur_y >= N:
                    continue
                if visited[cur_x][cur_y]:
                    continue
                if color != board[cur_x][cur_y]:
                    continue
                q.append([cur_x, cur_y, color])
                visited[cur_x][cur_y] = True

answer.append(cnt)

# 적록색약이 아님
visited = [[False] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        q = deque()
        q.append([i, j, board2[i][j]])
        visited[i][j] = True
        cnt += 1
        while q:
            x, y, color = q.popleft()
            for k in range(4):
                cur_x = x + dx[k]
                cur_y = y + dy[k]
                if cur_x < 0 or cur_x >= N or cur_y < 0 or cur_y >= N:
                    continue
                if visited[cur_x][cur_y]:
                    continue
                if color != board2[cur_x][cur_y]:
                    continue
                q.append([cur_x, cur_y, color])
                visited[cur_x][cur_y] = True

answer.append(cnt)

print(*answer)
