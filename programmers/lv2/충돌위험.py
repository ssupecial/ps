# 20:35~21:55
from collections import Counter


def check_duplicate(
    arr,
):  # 단순히 중복이 있냐만 체크하는게 아니라 중복하는 위치의 "개수"를 측정해야함
    nunique = Counter(arr)
    duplicate_count = 0
    for count in nunique.values():
        if count > 1:
            duplicate_count += 1
    return duplicate_count


def solution(points, routes):
    n_robots = len(routes)
    history = []
    times = []

    for i, robot in enumerate(routes):
        time = 0
        cur_x, cur_y = points[robot[0] - 1]
        robot_history = [[cur_x, cur_y]]
        for route in robot[1:]:
            dest_x, dest_y = points[route - 1]
            while cur_x != dest_x or cur_y != dest_y:
                if dest_x > cur_x:
                    cur_x += 1
                elif dest_x < cur_x:
                    cur_x -= 1
                elif dest_y > cur_y:
                    cur_y += 1
                elif dest_y < cur_y:
                    cur_y -= 1
                time += 1
                robot_history.append([cur_x, cur_y])
        history.append(robot_history)
        times.append(time)  # 각 로봇의 최대 시간 길이를 저장

    answer = 0

    for time in range(max(times) + 1):
        arr = []
        for j in range(n_robots):
            if time <= times[j]:
                arr.append((history[j][time][0], history[j][time][1]))

        answer += check_duplicate(arr)

    return answer


# solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])
solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]])
