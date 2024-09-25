# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

import itertools


def solution(orders, course):
    answer = []

    for num in course:
        result = {}

        for order in orders:
            arr = [_value for _value in order]
            choices = itertools.combinations(arr, num)
            choices = ["".join(sorted(choice)) for choice in choices]

            for choice in choices:
                result[choice] = result.get(choice, 0) + 1

        if len(result) > 0:
            # 주문 횟수로 정렬
            sorted_choices = sorted(result.items(), key=lambda x: x[1], reverse=True)
            max_num = sorted_choices[0][1]
            for i, (key, value) in enumerate(sorted_choices):
                if value >= 2:
                    if i == 0:
                        answer.append(key)
                    elif value == max_num:
                        answer.append(key)
                    else:  # 굳이 정답에 영향을 미치진 않지만 시간을 좀 줄일 수 있음
                        break
                else:  # 굳이 정답에 영향을 미치진 않지만 시간을 좀 줄일 수 있음
                    break

    return sorted(answer)
