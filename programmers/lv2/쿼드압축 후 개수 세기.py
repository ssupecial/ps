def count(arr):
    size = len(arr) ** 2
    count_one = sum([sum(row) for row in arr])
    count_zero = size - count_one

    same = False
    # 같은 값으로 채워져있다면 개수를 1로 만들기
    if count_one == size:
        same = True
        count_one = 1

    elif count_zero == size:
        same = True
        count_zero = 1

    return same, {0: count_zero, 1: count_one}


def split(arr):
    """
    first | second
    third | fourth
    """
    n = len(arr)

    first_part = [row[: n // 2] for row in arr[: n // 2]]
    second_part = [row[n // 2 :] for row in arr[: n // 2]]
    third_part = [row[: n // 2] for row in arr[n // 2 :]]
    fourth_part = [row[n // 2 :] for row in arr[n // 2 :]]

    return first_part, second_part, third_part, fourth_part


def recur(arr):
    same, counter = count(arr)
    if same:
        return counter

    first_part, second_part, third_part, fourth_part = split(arr)

    first_counter = recur(first_part)
    second_counter = recur(second_part)
    third_counter = recur(third_part)
    fourth_counter = recur(fourth_part)

    counter = {
        0: first_counter.get(0)
        + second_counter.get(0)
        + third_counter.get(0)
        + fourth_counter.get(0),
        1: first_counter.get(1)
        + second_counter.get(1)
        + third_counter.get(1)
        + fourth_counter.get(1),
    }

    return counter


def solution(arr):
    answer = recur(arr)
    answer = [answer.get(0), answer.get(1)]
    return answer


answer = solution(
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
    ]
)

# answer = solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print(answer)
