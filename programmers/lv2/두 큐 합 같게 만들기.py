# LV 2: 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    sum_all = sum1 + sum2

    if (sum1 + sum2) % 2 == 1:
        return -1

    half_sum = (sum1 + sum2) / 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    max_num = len(queue1) * 4
    answer = 0

    while answer <= max_num:

        if sum1 == half_sum:
            return answer
        elif len(queue1) == 0 or len(queue2) == 0:
            answer = -1
            break
        elif sum1 > half_sum:
            cur = queue1.popleft()
            sum1 -= cur
            queue2.append(cur)
        elif sum1 < half_sum:
            cur = queue2.popleft()
            sum1 += cur
            queue1.append(cur)

        answer += 1

    return answer


answer = solution([3, 2, 7, 2], [4, 6, 5, 1])
print(answer)
