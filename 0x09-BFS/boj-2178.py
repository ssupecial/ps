from collections import deque

n, m = list(map(int, input().split()))
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

board = []
for _ in range(n):
    board.append(list(map(int, input())))

q = deque()
q.append([0, 0])
visited[0][0] = True
dist[0][0] = 1

while q:
    x, y = q.popleft()
    distance = dist[x][y] + 1

    for i in range(4):
        cur_x = x + dx[i]
        cur_y = y + dy[i]

        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
            continue
        if not visited[cur_x][cur_y] and board[cur_x][cur_y] == 1:
            q.append([cur_x, cur_y])
            visited[cur_x][cur_y] = True
            dist[cur_x][cur_y] = distance

print(dist[n - 1][m - 1])
