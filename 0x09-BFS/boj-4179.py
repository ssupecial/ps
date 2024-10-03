from collections import deque

n, m = list(map(int, input().split()))
board = []
j_queue = deque()
f_queue = deque()

j_visited = [[False] * m for _ in range(n)]
j_dist = [[-1] * m for _ in range(n)]

f_visited = [[False] * m for _ in range(n)]
f_dist = [[-1] * m for _ in range(n)]


for i in range(n):
    cur = list(input())
    board.append(cur)
    for j in range(m):
        if cur[j] == "J":
            j_queue.append([i, j])
            j_dist[i][j] = 0
            j_visited[i][j] = True
        if cur[j] == "F":
            f_queue.append([i, j])
            f_dist[i][j] = 0
            f_visited[i][j] = True

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while f_queue:
    x, y = f_queue.popleft()
    distance = f_dist[x][y] + 1
    for i in range(4):
        cur_x = x + dx[i]
        cur_y = y + dy[i]

        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
            continue
        if not f_visited[cur_x][cur_y] and board[cur_x][cur_y] != "#":
            f_queue.append([cur_x, cur_y])
            f_visited[cur_x][cur_y] = True
            f_dist[cur_x][cur_y] = distance

while j_queue:
    x, y = j_queue.popleft()
    distance = j_dist[x][y] + 1
    for i in range(4):
        cur_x = x + dx[i]
        cur_y = y + dy[i]

        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
            print(distance)
            exit()
        if j_visited[cur_x][cur_y] or board[cur_x][cur_y] == "#":
            continue
        if f_dist[cur_x][cur_y] != -1 and f_dist[cur_x][cur_y] <= distance:
            continue

        j_queue.append([cur_x, cur_y])
        j_visited[cur_x][cur_y] = True
        j_dist[cur_x][cur_y] = distance


print("IMPOSSIBLE")
