def solution(n, m, x, y, r, c, k):
    fast_path = abs(x - r) + abs(y - c)
    if k < fast_path or (k - fast_path) % 2 != 0:
        return "impossible"

    op_counts = {"d": 0, "u": 0, "l": 0, "r": 0}

    rest = 0
    if x > r:
        op_counts["u"] = x - r
        rest += x - r
    elif x < r:
        op_counts["d"] = r - x
        rest += r - x
    if y > c:
        op_counts["l"] = y - c
        rest += y - c
    elif y < c:
        op_counts["r"] = c - y
        rest += c - y

    rest = k - rest
    result = ""

    while len(result) < k:
        if x < n and (op_counts["d"] > 0 or rest > 0):
            if op_counts["d"] > 0:
                op_counts["d"] -= 1
            elif rest > 0:
                rest -= 2
                op_counts["u"] += 1
            result += "d"
            x += 1
        elif y > 1 and (op_counts["l"] > 0 or rest > 0):
            if op_counts["l"] > 0:
                op_counts["l"] -= 1
            elif rest > 0:
                rest -= 2
                op_counts["r"] += 1
            result += "l"
            y -= 1
        elif y < m and (op_counts["r"] > 0 or rest > 0):
            if op_counts["r"] > 0:
                op_counts["r"] -= 1
            elif rest > 0:
                rest -= 2
                op_counts["l"] += 1
            result += "r"
            y += 1
        elif x > 1 and (op_counts["u"] > 0 or rest > 0):
            if op_counts["u"] > 0:
                op_counts["u"] -= 1
            elif rest > 0:
                rest -= 2
                op_counts["d"] += 1
            result += "u"
            x += 1

    answer = result

    return answer


"""위의 코드를 리팩토링한 버전"""


def solution_refac(n, m, x, y, r, c, k):
    # 최단 거리 계산
    min_distance = abs(x - r) + abs(y - c)

    # 불가능한 경우 체크
    if k < min_distance or (k - min_distance) % 2 != 0:
        return "impossible"

    # 방향별 필요한 이동 횟수 초기화
    moves = {
        "d": max(0, r - x),  # 아래로 가야 하는 횟수
        "u": max(0, x - r),  # 위로 가야 하는 횟수
        "l": max(0, y - c),  # 왼쪽으로 가야 하는 횟수
        "r": max(0, c - y),  # 오른쪽으로 가야 하는 횟수
    }

    # 남은 이동 횟수
    remaining = k - sum(moves.values())

    # 사전순으로 가능한 이동을 체크하는 함수
    def can_move(direction, curr_x, curr_y):
        if direction == "d":
            return curr_x < n and (moves["d"] > 0 or remaining > 0)
        if direction == "l":
            return curr_y > 1 and (moves["l"] > 0 or remaining > 0)
        if direction == "r":
            return curr_y < m and (moves["r"] > 0 or remaining > 0)
        if direction == "u":
            return curr_x > 1 and (moves["u"] > 0 or remaining > 0)

    # 이동을 수행하는 함수
    def make_move(direction, curr_x, curr_y):
        nonlocal remaining
        if moves[direction] > 0:
            moves[direction] -= 1
        else:
            remaining -= 2
            # 반대 방향으로 돌아가는 이동 추가
            opposite = {"d": "u", "u": "d", "l": "r", "r": "l"}
            moves[opposite[direction]] += 1

        # 현재 위치 업데이트
        if direction == "d":
            return curr_x + 1, curr_y
        if direction == "l":
            return curr_x, curr_y - 1
        if direction == "r":
            return curr_x, curr_y + 1
        if direction == "u":
            return curr_x - 1, curr_y

    # 경로 생성
    path = ""
    curr_x, curr_y = x, y

    # 사전순으로 이동 ('d' -> 'l' -> 'r' -> 'u')
    while len(path) < k:
        for direction in ["d", "l", "r", "u"]:
            if can_move(direction, curr_x, curr_y):
                curr_x, curr_y = make_move(direction, curr_x, curr_y)
                path += direction
                break

    return path


"""
시간 초과

from itertools import product


def solution(n, m, x, y, r, c, k):
    fast_path = abs(x - r) + abs(y - c)
    if k < fast_path or (k - fast_path) % 2 != 0:
        return "impossible"
    paths = list(product(["d", "l", "r", "u"], repeat=k))
    paths.sort()
    answer = ""
    for path in paths:
        cur_x = x
        cur_y = y
        result = ""
        for operator in path:
            if operator == "d":
                cur_x += 1
            elif operator == "l":
                cur_y -= 1
            elif operator == "r":
                cur_y += 1
            else:
                cur_x -= 1

            if cur_x < 1 or cur_x > n or cur_y < 1 or cur_y > m:
                break

            result += operator

        if cur_x == r and cur_y == c and len(result) == k:
            answer = result
            break

    if answer == "":
        answer = "impossible"

    return answer
"""

solution(3, 4, 2, 3, 3, 1, 5)
solution(2, 2, 1, 1, 2, 2, 2)
solution(3, 3, 1, 2, 3, 3, 4)
