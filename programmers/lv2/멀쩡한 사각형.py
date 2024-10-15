# Lv2 멀쩡한 사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 10.15 화요일 21:20~


import math


# 1차 풀이 - 83
def solution2(w, h):

    minus = 0

    max_tmp = max(w, h)
    min_tmp = min(w, h)
    w = max_tmp
    h = min_tmp
    for i in range(w):
        l = math.floor(h * i / w)
        r = math.ceil(h * (i + 1) / w)
        minus += r - l

        print(r - l)

    return w * h - minus


# 2차 풀이 - 87
def solution(w, h):
    if w == 1 or h == 1:
        return 0
    x = max(w, h)
    y = min(w, h)
    index = 1

    two = 0
    one = 0
    median = 0
    while True:
        a = math.ceil(x * index / y)
        if a > math.ceil(x / 2):
            break
        if (x * index) % y == 0:
            if a == math.ceil(x / 2):
                median = 1
            else:
                one += 1
        else:
            if a == math.ceil(x / 2):
                median = 2
            else:
                two += 1

        index += 1

    if x % 2 == 0:
        rest_one = x // 2 - (two + one + median)
        result = (rest_one + one + median + two * 2) * 2
    else:
        rest_one = x // 2 - (two + one)
        median = 1 if median == 0 else median
        result = (rest_one + one + two * 2) * 2 + median
    return w * h - result


# 최종 정답
def solution(w, h):
    k = math.gcd(w, h)
    return w * h - (w + h - k)


answer = solution(15, 7)
answer2 = solution2(15, 7)
print(answer, answer2)
