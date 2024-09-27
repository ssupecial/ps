# 거리두기 확인하기 (BFS 버전)
# https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 14:50~15:20 (30분)

from collections import deque


def bfs(people, place):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    dist = [[99] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    x, y = people
    q.append([x, y])
    dist[x][y] = 0
    visited[x][y] = True

    while q:
        x, y = q.pop()
        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            cur_dist = dist[x][y]

            if cur_x < 0 or cur_x > 4 or cur_y < 0 or cur_y > 4:
                continue
            else:
                if (
                    place[cur_x][cur_y] == "P"
                    and cur_dist < 2
                    and not visited[cur_x][cur_y]
                ):
                    return 0

                if (
                    place[cur_x][cur_y] != "X"
                    and cur_dist < 2
                    and not visited[cur_x][cur_y]
                ):
                    q.append([cur_x, cur_y])
                    dist[cur_x][cur_y] = cur_dist + 1
                    visited[cur_x][cur_y] = True

    return 1


def solution(places):
    answer = []

    for place in places:
        corr = 1
        peoples = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    peoples.append([i, j])

        for people in peoples:
            result = bfs(people, place)
            if result == 0:
                corr = 0
                break

        answer.append(corr)
    return answer


solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
)
