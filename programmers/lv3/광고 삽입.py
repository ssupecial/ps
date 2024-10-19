def convert_seconds(time):
    h, m, s = map(int, time.split(":"))
    return h * 60 * 60 + m * 60 + s


def convert_from_seconds(time):
    s = time % 60
    m = time // 60 % 60
    h = time // 3600
    return f"{h:0>2}:{m:0>2}:{s:0>2}"


def solution(play_time, adv_time, logs):

    time_durations = [0] * (convert_seconds(play_time) + 1)

    for log in logs:
        start_time, end_time = map(convert_seconds, log.split("-"))

        time_durations[start_time] += 1
        time_durations[end_time] -= 1

    for i in range(1, len(time_durations)):
        time_durations[i] = time_durations[i] + time_durations[i - 1]

    for i in range(1, len(time_durations)):
        time_durations[i] = time_durations[i] + time_durations[i - 1]

    adv_time_second = convert_seconds(adv_time)
    play_time_second = convert_seconds(play_time)

    answer = 0
    max_total = time_durations[adv_time_second - 1]
    for i in range(0, len(time_durations) - adv_time_second):
        total = time_durations[i + adv_time_second] - time_durations[i]
        if max_total < total:
            max_total = total
            answer = i + 1

    return convert_from_seconds(answer)


# solution(
#     "02:03:55",
#     "00:14:15",
#     [
#         "01:20:15-01:45:14",
#         "00:40:31-01:00:00",
#         "00:25:50-00:48:29",
#         "01:30:59-01:53:29",
#         "01:37:44-02:02:30",
#     ],
# )
answer = solution(
    "99:59:59",
    "25:00:00",
    [
        "69:59:59-89:59:59",
        "01:00:00-21:00:00",
        "79:59:59-99:59:59",
        "11:00:00-31:00:00",
    ],
)

# answer = solution(
#     "50:00:00",
#     "50:00:00",
#     ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
# )
print(answer)


# print(convert_seconds("01:37:44"))
# print(convert_seconds("01:45:14"))
