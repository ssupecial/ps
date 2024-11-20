from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]
    oil = [[0] * m for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    answers = [0] * m

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                arr = []
                q = deque()
                q.append([i, j])
                visited[i][j] = True

                while q:
                    x, y = q.pop()
                    arr.append(y)
                    for k in range(4):
                        cur_x = x + dx[k]
                        cur_y = y + dy[k]

                        if cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= m:
                            continue
                        if visited[cur_x][cur_y] or land[cur_x][cur_y] == 0:
                            continue

                        q.append([cur_x, cur_y])
                        visited[cur_x][cur_y] = True

                size = len(arr)
                if size > 0:
                    for y in set(arr):
                        answers[y] += size

    answer = max(answers)

    return answer


solution(
    [
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1],
    ]
)
