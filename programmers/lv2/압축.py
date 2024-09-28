# 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# 9.28 18:50~19:10

import string


def solution(msg):
    dict = {}
    upper_list = string.ascii_uppercase
    for i, w in enumerate(upper_list):
        dict[w] = i + 1

    answer = []
    max_num = 27

    while msg:
        start = 0
        finish = 1
        while dict.get(msg[start:finish], "") != "":
            finish += 1
            if finish > len(msg):
                break

        finish -= 1
        cur = msg[start:finish]

        answer.append(dict[cur])

        # 사전에 추가
        dict[msg[start : finish + 1]] = max_num
        max_num += 1
        msg = msg[finish:]

        # print("Cur: ", cur, "Add: ", msg[start : finish + 1], "Msg: ", msg)

    return answer


solution("TOBEORNOTTOBEORTOBEORNOT")
