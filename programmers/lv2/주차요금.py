# 주차요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341


import math


def calculate_mins(start_hour, start_min, fin_hour, fin_min):
    # 두 개의 시간대를 받아서 시간차이 계산하는 함수
    return (fin_hour * 60) + fin_min - (start_hour * 60) - start_min


def solution(fees, records):
    default_min, default_price, unit_min, unit_price = fees

    answer = []
    records_per_car = {}

    for record in records:
        time, car, type = record.split()
        hour, min = list(map(int, time.split(":")))
        if car not in records_per_car.keys():
            records_per_car[car] = [(hour, min)]
        else:
            records_per_car[car].append((hour, min))

    for key, value in records_per_car.items():
        if len(value) % 2 == 1:
            value.append((23, 59))

        duration_sum = 0
        for i in range(0, len(value), 2):
            duration = calculate_mins(
                value[i][0], value[i][1], value[i + 1][0], value[i + 1][1]
            )
            duration_sum += duration

        if duration_sum <= default_min:
            pay = default_price
        else:
            pay = (
                default_price
                + math.ceil((duration_sum - default_min) / unit_min) * unit_price
                # default_price + ((duration_sum - default_min + unit_min - 1) // unit_min) * unit_price
            )

        answer.append((key, pay))

    # 번호판 순서대로 튜플 배열을 정렬하고 요금만 출력
    return [value[1] for value in sorted(answer, key=lambda x: x[0])]
