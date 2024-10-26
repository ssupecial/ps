from collections import Counter


def count(arr):
    counter = Counter()
    for row in arr:
        tmp = Counter(row)
        counter.update(tmp)

    if len(counter.keys()) == 1:
        counter = Counter({arr[0][0]: 1})

    return counter


def recur(arr):
    n = len(arr)

    first_part = [row[: n // 2] for row in arr[: n // 2]]
    second_part = [row[n // 2 :] for row in arr[: n // 2]]
    third_part = [row[: n // 2] for row in arr[n // 2 :]]
    fourth_part = [row[n // 2 :] for row in arr[n // 2 :]]

    counter = Counter()

    first_counter = count(first_part)
    if len(first_counter.keys()) > 1:
        first_counter = recur(first_part)
    second_counter = count(second_part)
    if len(second_counter.keys()) > 1:
        second_counter = recur(second_part)
    third_counter = count(third_part)
    if len(third_counter.keys()) > 1:
        third_counter = recur(third_part)
    fourth_counter = count(fourth_part)
    if len(fourth_counter.keys()) > 1:
        fourth_counter = recur(fourth_part)

    counter.update(first_counter)
    counter.update(second_counter)
    counter.update(third_counter)
    counter.update(fourth_counter)

    return counter


def solution(arr):
    answer = recur(arr)
    answer = [answer.get(0, 0), answer.get(1, 0)]
    print(answer)
    return answer
