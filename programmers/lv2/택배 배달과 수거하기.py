# 택배 배달과 수거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 09.26 23:25~00:45 (1시간 20분)


def solution(cap, n, deliveries, pickups):
    """
    모범 답안 확인
    """
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    delivery_cur = 0
    pickup_cur = 0
    for i in range(n):
        delivery_cur += deliveries[i]
        pickup_cur += pickups[i]

        while delivery_cur > 0 or pickup_cur > 0:
            delivery_cur -= cap
            pickup_cur -= cap
            answer += 2 * (n - i)

    print(answer)
    """
    1차 시도 - 0점
    delivery_index = n - 1
    pickup_index = n - 1
    answer = 0

    delivery_cur = 0
    pickup_cur = 0
    while delivery_index > 0 or pickup_index > 0:
        answer += 2 * (max(delivery_index, pickup_index) + 1)
        while True:
            if deliveries[delivery_index] > (cap - delivery_cur) or delivery_index < 0:
                break
            if deliveries[delivery_index] <= (cap - delivery_cur):
                delivery_cur += deliveries[delivery_index]
                delivery_index -= 1
            else:  # deliveries[delivery_index] > (cap - delivery_cur)
                delivery_cur += cap - delivery_cur
                deliveries[delivery_index] -= cap - delivery_cur

        delivery_cur = 0

        while True:
            if pickups[pickup_index] > (cap - pickup_cur) or pickup_index < 0:
                break
            if pickups[pickup_index] <= (cap - pickup_cur):
                pickup_cur += pickups[pickup_index]
                pickup_index -= 1
            else:  # deliveries[delivery_index] > (cap - delivery_cur)
                pickup_cur += cap - pickup_cur
                pickups[pickup_index] -= cap - pickup_cur

        pickup_cur = 0

    return answer
    """

    """
    2차 시도 - 50점
    answer = 0

    delivery_changes = []
    delivery_sum = 0
    delivery_change_ = -1
    for idx, num in enumerate(list(reversed(deliveries))):
        delivery_sum += num
        if (delivery_sum - 1) // cap != delivery_change_:
            delivery_change_ = (delivery_sum - 1) // cap
            delivery_changes.append(n - idx)

    pickup_changes = []
    pickup_sum = 0
    pickup_change_ = -1
    for idx, num in enumerate(list(reversed(pickups))):
        pickup_sum += num
        if (pickup_sum - 1) // cap != pickup_change_:
            pickup_change_ = (pickup_sum - 1) // cap
            pickup_changes.append(n - idx)

    min_length = min(len(pickup_changes), len(delivery_changes))
    for j in range(min_length):
        answer += max(delivery_changes[j], pickup_changes[j])

    for j in range(min_length, len(pickup_changes)):
        answer += pickup_changes[j]
    for j in range(min_length, len(delivery_changes)):
        answer += delivery_changes[j]

    return answer * 2
    """


# solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
