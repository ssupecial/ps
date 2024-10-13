# https://school.programmers.co.kr/learn/courses/30/lessons/181187#
# 10.13 13:45~14:35 (50분)
def solution(r1, r2):
    import math

    answer = 0
    r1_sq = r1**2
    r2_sq = r2**2

    for i in range(1, r2 + 1):
        y_max = math.floor(math.sqrt(r2_sq - i**2))
        y_min = math.ceil(math.sqrt(r1_sq - i**2)) if i <= r1 else 0
        answer += y_max - y_min + 1

    return answer * 4
