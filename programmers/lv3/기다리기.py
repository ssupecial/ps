# 40분 소요
import heapq

arr = []  # 각 유형별 멘토의 수
waiting_time = float("inf")


def waiting_per_type(people, waits):  # 각 유형별 대기 시간 계산
    cur = 0
    time = 0
    finish = []
    for start, duration in waits:
        if cur < people:
            cur += 1
            heapq.heappush(finish, start + duration)
        else:
            tmp = heapq.heappop(finish)
            if tmp > start:
                time += tmp - start
                heapq.heappush(finish, tmp + duration)
            else:
                heapq.heappush(finish, start + duration)

    return time


def calculate(k):  # 전체 대기 시간 계산
    global waiting_list
    sum_time = 0
    for i in range(k):
        sum_time += waiting_per_type(arr[i], waiting_list[i])
    return sum_time


def func(depth, cur, k, n):  # 백트래킹으로 각 유형별 멘토의 수 조합을 모두 계산함
    global waiting_time
    if depth == k:
        if cur == n:
            time = calculate(k)
            if waiting_time > time:
                waiting_time = time
        return

    for i in range(1, n + 1):
        if cur + i > n:  # 배정 가능한 멘토의 수를 다 써버림
            break
        arr.append(i)
        func(depth + 1, cur + i, k, n)
        arr.pop()


def solution(k, n, reqs):
    global waiting_list
    waiting_list = [[] for _ in range(k)]
    for start, duration, type in reqs:
        waiting_list[type - 1].append([start, duration])

    func(0, 0, k, n)
    return waiting_time


# answer = solution(
#     3,
#     5,
#     [
#         [10, 60, 1],
#         [15, 100, 3],
#         [20, 30, 1],
#         [30, 50, 3],
#         [50, 40, 1],
#         [60, 30, 2],
#         [65, 30, 1],
#         [70, 100, 2],
#     ],
# )
# answer = solution(
#     2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
# )

answer = solution(1, 1, [[5, 55, 1]])
print(answer)
